const fs = require('fs');
const axios = require('axios');
const path = require('path');

// Lista e URL-ve për të marrë proxy
const urls = [
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
    'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
    'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
    'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
    'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
    'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
    'https://api.openproxylist.xyz/http.txt',
    'https://api.proxyscrape.com/v2/?request=displayproxies',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
    'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
    'http://worm.rip/http.txt',
    'https://proxyspace.pro/http.txt',
    'https://multiproxy.org/txt_all/proxy.txt',
    'https://proxy-spider.com/api/proxies.example.txt',
];

// Funksioni për të marrë të dhënat nga proxy dhe ruajti ato në një skedar
async function fetchProxies() {
    const file = path.resolve(__dirname, 'proxy.txt');

    try {
        if (fs.existsSync(file)) {
            fs.unlinkSync(file); // Fshijë skedarin nëse ekziston
            console.log(`\x1b[31mFile\x1b[0m ${file} \x1b[33mNe file\x1b[0m \x1b[32mProxyt\x1b[0m \n`);
        }

        const proxyData = [];

        for (const url of urls) {
            try {
                const response = await axios.get(url);
                proxyData.push(response.data);
                console.log(` -| sukses \x1b[32m${url}\x1b[0m`);
            } catch (error) {
                console.error(` -| gabim \x1b[31m${url}\x1b[0m`);
            }
        }

        fs.writeFileSync(file, proxyData.join('\n'), 'utf8');

        const total = (await fs.promises.readFile(file, 'utf8')).split('\n').length;
        console.log(`\n\x1b[37m( \x1b[33m${total}\x1b[37m ) \x1b[32mProxy u moren.\x1b[0m`);

    } catch (error) {
        console.error('Ndodhi një gabim:', error);
    }
}

fetchProxies();
