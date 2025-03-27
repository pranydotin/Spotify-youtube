import ytmusicapi
ytmusicapi.setup(filepath="browser.json", headers_raw="""POST /youtubei/v1/browse?prettyPrint=false HTTP/2
Host: music.youtube.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br, zstd
Content-Type: application/json
Content-Length: 3051
Referer: https://music.youtube.com/
X-Goog-Visitor-Id: CgtjQTV4Qk9YcHhtNCjb24i_BjIKCgJJThIEGgAgDw%3D%3D
X-Youtube-Bootstrap-Logged-In: true
X-Youtube-Client-Name: 67
X-Youtube-Client-Version: 1.20250317.01.00
X-Goog-AuthUser: 0
X-Origin: https://music.youtube.com
Origin: https://music.youtube.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: same-origin
Sec-Fetch-Site: same-origin
Authorization: SAPISIDHASH 1742876217_285d10e34b604f58dadda8e2b336df6c8cf16108_u SAPISID1PHASH 1742876217_285d10e34b604f58dadda8e2b336df6c8cf16108_u SAPISID3PHASH 1742876217_285d10e34b604f58dadda8e2b336df6c8cf16108_u
Connection: keep-alive
Alt-Used: music.youtube.com
Cookie: SID=g.a000vAgQ-W2Tf0MCpe9gAXbaDZS58RL2B0JPwR6ggpnYfVXzVXJn2FL4--GiRLacjnkjCUBqXgACgYKAUASARQSFQHGX2Mi0TLve_ZRNGCX_WSDI43g5xoVAUF8yKpWAWTYWTrDdWLeMJ1KKQV70076; __Secure-1PSIDTS=sidts-CjEB7pHptSkX5kSjueEqQYyfbGkPQs33xwW1uK4lh3sqHCEGYxfS6MHsza9PEid4_huGEAA; __Secure-3PSIDTS=sidts-CjEB7pHptSkX5kSjueEqQYyfbGkPQs33xwW1uK4lh3sqHCEGYxfS6MHsza9PEid4_huGEAA; __Secure-1PSID=g.a000vAgQ-W2Tf0MCpe9gAXbaDZS58RL2B0JPwR6ggpnYfVXzVXJnYFu82IGedMuCuS_PvqE54AACgYKATUSARQSFQHGX2MiY6hENdaFPH_suerMgET3kRoVAUF8yKp6hzboSc0_CZZMOI2nwTA20076; __Secure-3PSID=g.a000vAgQ-W2Tf0MCpe9gAXbaDZS58RL2B0JPwR6ggpnYfVXzVXJnmp82elgkN5ruonwTc6Ii1AACgYKAW0SARQSFQHGX2Mif0s2EaooTvxidEZ_R0pdEBoVAUF8yKph0-TrRS0_wszuxTTajpcg0076; HSID=ApRuvSEANNzMx97Io; SSID=AsplhYhrEsTCSI7EJ; APISID=71mRfbCVdqiXBH7M/AGEkc0Sd2r-IZFMCu; SAPISID=rW7rVmXxUfXPARo6/AdDCy5Echto40Pk-k; __Secure-1PAPISID=rW7rVmXxUfXPARo6/AdDCy5Echto40Pk-k; __Secure-3PAPISID=rW7rVmXxUfXPARo6/AdDCy5Echto40Pk-k; VISITOR_INFO1_LIVE=cA5xBOXpxm4; VISITOR_PRIVACY_METADATA=CgJJThIEGgAgDw%3D%3D; __Secure-ROLLOUT_TOKEN=CKXwlKLwxaizWhC4od2H5ceLAxjAk-T0w6OMAw%3D%3D; SIDCC=AKEyXzU9NJGqzU9O8OCLNnsKQRtcxQihJvsTQG0HG9teWp6GxAuDLcAcas8-Zydki7r0JtsQKw; __Secure-1PSIDCC=AKEyXzV-Fi3CTb_wEf7blUcLO9CfHAPxbSo6PdBZc6duZ9UI3V0Ta0_inCYzplse5yd57YPBkg; __Secure-3PSIDCC=AKEyXzXq4rZQOkEkXeXxAjCcrc9M3RtNOaKIKAs9Xw3fFmS_eDPOtMkjKHKwFIYFN1Y387Y2Ar4; PREF=f4=4000000&f6=40000000&tz=Asia.Kolkata&f5=30000&f7=100&repeat=NONE; LOGIN_INFO=AFmmF2swRAIgUTltCmM-sR-5UhLIGx_Gu6NYRsCYRB-4zXFFog1lFGkCIHXQleo3ktWa5K3sWbqH9eZhuQEymvorL1ofLdayQ476:QUQ3MjNmd1FDN1VuaHJUb2FwNjRtYlB2ZXNaQUFldFppR3ktdTF2cllDMTZaMnlNZ05IVERxd0JBanMwemljZExycUdWdGlnd0o3SllBZllWQmhCUlJWbGFTQWFTT3V4R0p1LThCYWxhQUF6YmhnbXc5SDB0UEhGclROSUpiZ2tJUkRpSnpXYzlabTc2MHczMTdlSC1MMnhBMjBsb2JmQTN3; _gcl_au=1.1.1868317805.1742192384; _ga_VCGEPY40VB=GS1.1.1742194650.2.0.1742194650.60.0.0; _ga=GA1.1.144273737.1742192432; NID=522=0MzDtiuqsfrtH22L38DPYMHi2rv0bci_XL4jUIGhHg0OOPAIQiCqL_bnUmC0X0OJ5X4vzRDrQLJ2qLHvOOrPBEI_c6mWSGOfomOuN2BvbaMNBHCD1iwYBRqsxmdBbw3bykFRlqwRMXr3718swjmMrF-6s77uhVHyHyzZnvNIxtbd1-hdgYmMD2fVLzpvb2S6DZhdOwIVxrYny_LWQG4O2V5X; YSC=Qa9iOuEOhig
Priority: u=0
TE: trailers""")


# "authorization": "SAPISIDHASH 1742876217_285d10e34b604f58dadda8e2b336df6c8cf16108_u SAPISID1PHASH 1742876217_285d10e34b604f58dadda8e2b336df6c8cf16108_u SAPISID3PHASH 1742876217_285d10e34b604f58dadda8e2b336df6c8cf16108_u",
