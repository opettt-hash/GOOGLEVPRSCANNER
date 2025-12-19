#!/usr/bin/env python3
#Nusatenggara Timur Development Coded By Rolandino
import os, re, time, math, json
from urllib.parse import urljoin, urlparse
from datetime import datetime, timezone
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.panel import Panel



DELAY = 1.0
TIMEOUT = 6
MAX_JS = 200
OUTPUT_DIR = "vrp_output"

console = Console()

HEADERS = {
    
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36 "
        "GoogleVRP-PassiveResearch/2.1"
    ),

    
    "Accept": (
        "text/html,application/xhtml+xml,"
        "application/xml;q=0.9,"
        "application/javascript,text/javascript,"
        "application/json,"
        "*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "utf-8",
    "Accept-Encoding": "gzip, deflate, br",

    
    "Cache-Control": "no-cache, no-store, max-age=0",
    "Pragma": "no-cache",
    "If-None-Match": "",
    "If-Modified-Since": "0",

    
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-User": "?1",
    "Sec-Ch-Ua": '"Chromium";v="121", "Google Chrome";v="121", "Not;A=Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',

    
    "Priority": "u=0, i",

    
    "Referer": "https://developers.google.com/",
    "Origin": "https://developers.google.com",
    "Dnt": "1",
    "Connection": "keep-alive",

    
    "X-Research-Purpose": "security-research",
    "X-Research-Method": "passive-js-analysis",
    "X-Research-Scope": "public-resources-only",
    "X-Research-Policy": "google-vrp-compliant",

    
    "TE": "trailers",
    "Accept-Encoding": "gzip, deflate, br"
}



KEYWORDS = [k.lower() for k in [

    
    "internal","private","confidential","restricted","classified",
    "corp","corporate","employee","staff","member","partner","vendor",
    "nonprod","non-prod","preprod","pre-prod",
    "sandbox","preview","staging","stage","test","testing","qa","uat",
    "beta","canary","experimental","nightly","dev","development",
    "demo","trial","sample","mock","fake","tmp","temp","temporary",
    "legacy","deprecated","old","unused","backup","bak","copy","clone",

    
    "auth","authentication","authorization","login","logout","signin","signup",
    "sso","mfa","2fa","totp","otp","webauthn","passkey",
    "oauth","oauth2","openid","oidc",
    "jwt","jws","jwe","bearer","basic","digest",
    "token","access_token","refresh_token","id_token","session","sessionid",
    "sid","csrf","xsrf","state","nonce",
    "clientid","client_id","clientsecret","client_secret",
    "apikey","api_key","secret","secrets","password","passwd","pwd",
    "passphrase","credential","credentials","key","keys",

    
    "env",".env",".env.local",".env.dev",".env.prod",
    "config","configuration","settings","options","preferences",
    "config.json","settings.json","manifest.json","package.json",
    "appsettings.json","config.yaml","config.yml",
    "settings.yaml","settings.yml",
    "manifest.yaml","manifest.yml",
    "credentials.json","serviceaccount.json",
    "key.json","keys.json",
    "sourcemap","sourcemaps","sourcemappingurl",
    "webpack","vite","rollup","parcel","babel","tsconfig","jsconfig",

    
    "api","apis","endpoint","endpoints",
    "rest","restapi","graphql","gql","graphiql",
    "rpc","grpc","jsonrpc","soap",
    "proto","protobuf","thrift","avro",
    "schema","schemas",
    "swagger","swaggerui","openapi",
    "version","versions","v0","v1","v2","v3","v4","v5",
    "internalapi","privateapi","adminapi","partnerapi",
    "devapi","testapi","stagingapi","sandboxapi",

    
    "cloud","gcp","googlecloud",
    "firebase","firestore","realtime","firebaseio",
    "bigquery","pubsub","datastore","spanner",
    "cloudfunctions","functions","cloudrun","run",
    "appengine","app-engine",
    "gke","kubernetes","k8s","container","docker","image",
    "compute","vm","instance","instances","node","nodes",
    "storage","bucket","buckets","object","objects",
    "dataset","table","tables","view","views",
    "serviceaccount","service_account",
    "iam","roles","permissions","policy","policies",
    "project","projectid","project_id",
    "organization","org","folder",
    "billing","quota","limits","usage",
    "region","regions","zone","zones","location","locations",

    
    "admin","administrator","administration",
    "adminpanel","admin_panel","adminconsole","admin_console",
    "superadmin","superuser","root","owner",
    "dashboard","console","management","manage","controlpanel",
    "debug","debugging","debugmode",
    "trace","tracing","traceid",
    "log","logs","logging","logger",
    "verbose","stacktrace","stack","error","errors",
    "monitor","monitoring","metrics","telemetry","health","status",
    "stats","profiling","profiler","inspector",

    
    "ci","cd","cicd","pipeline","pipelines",
    "build","builds","release","releases","deploy","deployment",
    "artifact","artifacts","registry","repo","repository",
    "git","github","gitlab","bitbucket",
    "jenkins","circleci","travis","actions",
    "helm","terraform","packer","ansible",

    
    "android","ios","mobile","webview",
    "apk","aab","ipa",
    "bundle","resources","assets",
    "client","frontend","backend","server","service","worker",
    "serviceworker","sw.js","worker.js",

    
    "analytics","tracking","tracker","telemetry",
    "measurement","metrics","events",
    "ga","gtag","gtm","tagmanager",
    "ads","adservice","doubleclick","admob",

    
    "ml","ai","model","models",
    "training","inference","predict","prediction",
    "dataset","datasets","label","labels",
    "feature","features","embedding","vector",

    
    "user","users","userid","user_id","uid",
    "account","accounts","profile","profiles",
    "email","emails","username","loginname",
    "session","sessions","cookie","cookies",

    
    "security","secure","insecure",
    "policy","policies","compliance","audit","auditing",
    "encryption","decrypt","crypto","hash","salt",
    "rsa","ecdsa","aes","hmac","pem","p12","pfx","crt","cert","certificate",

    
    "todo","fixme","hack","workaround",
    "example","sampledata","testdata",
    "internalonly","do_not_use","do-not-use",
    "wip","draft","experimentalonly",
    "backup","snapshot","dump","export","import",
]]

ENDPOINT_PATTERNS = [
    
    r"/api/[a-zA-Z0-9_./-]{3,}",
    r"/apis/[a-zA-Z0-9_./-]{3,}",
    r"/rest/[a-zA-Z0-9_./-]{3,}",
    r"/graphql",
    r"/gql",
    r"/graphiql",
    r"/v\d+/[a-zA-Z0-9_./-]{2,}",
    r"/v\d+\.\d+/[a-zA-Z0-9_./-]{2,}",
    r"/version/[a-zA-Z0-9_./-]{2,}",
    r"/internal/[a-zA-Z0-9_./-]{2,}",
    r"/private/[a-zA-Z0-9_./-]{2,}",
    r"/_internal/[a-zA-Z0-9_./-]{2,}",
    r"/__internal__[a-zA-Z0-9_./-]{0,}",
    r"/admin/?[a-zA-Z0-9_./-]*",
    r"/console/?[a-zA-Z0-9_./-]*",
    r"/manage/?[a-zA-Z0-9_./-]*",
    r"/debug/?[a-zA-Z0-9_./-]*",
    r"/trace/?[a-zA-Z0-9_./-]*",
    r"/monitor/?[a-zA-Z0-9_./-]*",
    r"/dashboard/?[a-zA-Z0-9_./-]*",
    r"/superuser/?[a-zA-Z0-9_./-]*",
    r"/root/?[a-zA-Z0-9_./-]*",
    r"/system/?[a-zA-Z0-9_./-]*",

    
    r"/login",
    r"/logout",
    r"/signin",
    r"/signup",
    r"/auth/?[a-zA-Z0-9_./-]*",
    r"/oauth/?[a-zA-Z0-9_./-]*",
    r"/token/?[a-zA-Z0-9_./-]*",
    r"/refresh/?[a-zA-Z0-9_./-]*",
    r"/authorize/?[a-zA-Z0-9_./-]*",
    r"/session/?[a-zA-Z0-9_./-]*",
    r"/csrf/?[a-zA-Z0-9_./-]*",
    r"/xsrf/?[a-zA-Z0-9_./-]*",

    
    r"\?key=[A-Za-z0-9_\-]{10,}",
    r"\?api_key=[A-Za-z0-9_\-]{10,}",
    r"\?access_token=[A-Za-z0-9\.\-_]{10,}",
    r"\?client_id=[A-Za-z0-9\-_]{6,}",
    r"&api_key=[A-Za-z0-9_\-]{10,}",
    r"&access_token=[A-Za-z0-9\.\-_]{10,}",
    r"&client_id=[A-Za-z0-9_\-]{6,}",
    r"[?&]token=[A-Za-z0-9_\-]{10,}",

    
    r"ey[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+",
    r"[A-Za-z0-9_\-]{20,}",
    r"[a-f0-9]{32,64}",

    
    r"/firebase/[a-zA-Z0-9_./-]{2,}",
    r"/firestore/[a-zA-Z0-9_./-]{2,}",
    r"/realtime/[a-zA-Z0-9_./-]{2,}",
    r"/bigquery/[a-zA-Z0-9_./-]{2,}",
    r"/pubsub/[a-zA-Z0-9_./-]{2,}",
    r"/datastore/[a-zA-Z0-9_./-]{2,}",
    r"/cloudfunctions/[a-zA-Z0-9_./-]{2,}",
    r"/functions/[a-zA-Z0-9_./-]{2,}",
    r"/gke/[a-zA-Z0-9_./-]{2,}",
    r"/kubernetes/[a-zA-Z0-9_./-]{2,}",
    r"/container/[a-zA-Z0-9_./-]{2,}",
    r"/projects/[a-zA-Z0-9_./-]{2,}",
    r"/locations/[a-zA-Z0-9_./-]{2,}",
    r"/zones/[a-zA-Z0-9_./-]{2,}",
    r"/regions/[a-zA-Z0-9_./-]{2,}",

    
    r"/config/?[a-zA-Z0-9_./-]*",
    r"/configuration/?[a-zA-Z0-9_./-]*",
    r"/settings/?[a-zA-Z0-9_./-]*",
    r"/env/?[a-zA-Z0-9_./-]*",
    r"/environment/?[a-zA-Z0-9_./-]*",
    r"/\.env",
    r"/config\.json",
    r"/settings\.json",
    r"/manifest\.json",
    r"/credentials\.json",
    r"/serviceaccount\.json",
    r"/swagger\.json",
    r"/openapi\.json",
    r"/schema\.json",
    r"/featureflag/?[a-zA-Z0-9_./-]*",
    r"/feature_flags/?[a-zA-Z0-9_./-]*",

    
    r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
    r"[A-F0-9]{8}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{12}",
    r"[a-z0-9]{32,64}",
    r"[A-Z0-9]{32,64}",

    
    r"/debugmode",
    r"/devtools",
    r"/experimental",
    r"/betaaccess",
    r"/canarybuild",
    r"/nightlybuild",
    r"/testapi",
    r"/stagingapi",
    r"/sandboxapi",
    r"/trial",
    r"/wip",
    r"/draft",
    r"/internalonly",
    r"/do_not_use",
    r"/do-not-use",
    r"/mock",
    r"/fake",
    r"/tmp",
    r"/temp",
    r"/backup",
    r"/snapshot",
    r"/dump",
    r"/export",
    r"/import"
]

GOOGLE_SCOPE = [
    
    "google.com",
    "www.google.com",
    "google.co.id",
    "google.co.uk",
    "google.ca",
    "google.de",
    "google.fr",
    "google.com.au",
    "googleusercontent.com",
    "gstatic.com",
    "ggpht.com",

    
    "googleapis.com",
    "clients1.google.com",
    "clients2.google.com",
    "clients3.google.com",
    "clients4.google.com",
    "clients5.google.com",
    "clients6.google.com",
    "clients7.google.com",
    "clients8.google.com",
    "apis.google.com",
    "content.googleapis.com",
    "script.googleapis.com",

    
    "cloud.google.com",
    "cloudfunctions.net",
    "run.app",
    "appspot.com",
    "googlecloud.com",
    "gcp.gvt2.com",
    "compute.googleapis.com",
    "storage.googleapis.com",
    "bigquery.googleapis.com",
    "spanner.googleapis.com",
    "pubsub.googleapis.com",
    "datastore.googleapis.com",
    "container.googleapis.com",

    
    "firebaseio.com",
    "firebaseapp.com",
    "firebase.google.com",
    "firebasedatabase.app",
    "firebasehosting.com",
    "firebasestorage.googleapis.com",

    
    "lh3.googleusercontent.com",
    "lh4.googleusercontent.com",
    "lh5.googleusercontent.com",
    "lh6.googleusercontent.com",
    "cdn.jsdelivr.net",
    "ajax.googleapis.com",
    "fonts.googleapis.com",
    "fonts.gstatic.com",

    
    "accounts.google.com",
    "oauth2.googleapis.com",
    "securetoken.googleapis.com",
    "identitytoolkit.googleapis.com",
    "openidconnect.googleapis.com",
    "signin.google.com",
    "login.live.com",

    
    "googletagmanager.com",
    "google-analytics.com",
    "analytics.google.com",
    "doubleclick.net",
    "googlesyndication.com",
    "adservices.google.com",
    "pagead2.googlesyndication.com",

    
    "android.com",
    "developer.android.com",
    "play.google.com",
    "play.googleapis.com",
    "android.googleapis.com",
    "gms.googleapis.com",

    
    "developers.google.com",
    "source.developers.google.com",
    "issuetracker.google.com",
    "buganizer.corp.google.com",
    "opensource.google",
    "chrome.com",
    "chromium.org",
    "chromestatus.com",
    "web.dev",

    
    "maps.google.com",
    "maps.googleapis.com",
    "geo.googleapis.com",
    "earthengine.googleapis.com",

    
    "youtube.com",
    "youtube.googleapis.com",
    "m.youtube.com",
    "studio.youtube.com",
    "ytimg.com",
    "yt3.ggpht.com",

    
    "translate.googleapis.com",
    "vision.googleapis.com",
    "speech.googleapis.com",
    "texttospeech.googleapis.com",
    "language.googleapis.com",
    "ml.googleapis.com",
    "tensorboard.dev",
    "developers.google.ai",
    "ai.google",

    
    "sandbox.googleapis.com",
    "staging.googleapis.com",
    "alpha.googleapis.com",
    "beta.googleapis.com",
    "experimental.googleapis.com",

    
    "g.co",
    "goo.gl",
    "withgoogle.com",
    "about.google",
    "blog.google",
    "developers.google.ai",
    "workspace.google.com",
    "admin.google.com",
    "mail.google.com",
    "drive.google.com",
    "docs.google.com",
    "ads.google.com",
    "adservices.google.com",
]



def entropy(s):
    if not s: return 0
    freq = {c: s.count(c)/len(s) for c in set(s)}
    return -sum(p * math.log2(p) for p in freq.values())

def in_scope(url):
    netloc = urlparse(url).netloc
    return any(netloc.endswith(d) for d in GOOGLE_SCOPE)

def fetch(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        time.sleep(DELAY)
        return r
    except:
        return None



def extract_js(html, base):
    soup = BeautifulSoup(html, "html.parser")
    js = []
    for s in soup.find_all("script"):
        if s.get("src"):
            full = urljoin(base, s["src"])
            if in_scope(full):
                js.append(full)
        else:
            js.append({"inline": s.text[:6000]})
    return js[:MAX_JS]

def analyze_js(js):
    findings = []

    if isinstance(js, dict):
        text = js["inline"].lower()
        source = "inline"
    else:
        r = fetch(js)
        if not r: return findings
        text = r.text.lower()
        source = js

    for pat in ENDPOINT_PATTERNS:
        for m in re.findall(pat, text):
            e = entropy(m)
            score = 0
            if any(x in m for x in ["internal","private","admin"]): score += 2
            if e > 3.3: score += 1
            if "/v1" in m or "/v2" in m: score += 1

            severity = "INFO"
            if score == 2: severity = "LOW"
            elif score >= 3: severity = "MEDIUM"

            findings.append({
                "endpoint": m,
                "severity": severity,
                "entropy": round(e,2),
                "source": source
            })
    return findings



def banner():
    console.print(
        Panel.fit(
            "[green]• SIMPLE GOOGLE VRP AUTO PASSIVE SCANNER •[/]\n"
            "– Team Crackers Communitiy\n"
            "– Coded By 𝕽𝖔𝖑𝖆𝖓𝖉𝖎𝖓𝖔",
            border_style="green",
            padding=(0, 1)
        )
    )
def main():
    banner()
    target = console.input("[bold]Target Url (Onliy Https) : [/]").strip()

    r = fetch(target)
    if not r:
        console.print("[red]Target Unreachable[/]")
        return

    js_assets = extract_js(r.text, target)

    console.print(f"[green]Js Assets Found :[/] {len(js_assets)}")

    all_findings = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task("Scanning Js Files", total=len(js_assets))

        for js in js_assets:
            all_findings.extend(analyze_js(js))
            progress.advance(task)

    

    table = Table(title="Potential Endpoint Findings Passive")
    table.add_column("Severity", style="bold")
    table.add_column("Endpoint", overflow="fold")
    table.add_column("Entropy")
    table.add_column("Source", overflow="fold")

    for f in all_findings:
        color = "green"
        if f["severity"] == "LOW": color = "yellow"
        if f["severity"] == "MEDIUM": color = "red"

        table.add_row(
            f"[{color}]{f['severity']}[/]",
            f["endpoint"],
            str(f["entropy"]),
            f["source"]
        )

    console.print(table)

    

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M")

    with open(f"{OUTPUT_DIR}/findings_{ts}.json", "w") as f:
        json.dump(all_findings, f, indent=2)

    console.print(f"[bold green]Report Saved To {OUTPUT_DIR}/[/]")

if __name__ == "__main__":
    main()