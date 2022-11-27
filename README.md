# GeekGame 2022 WriteUp 

> by hangyi

今年没怎么打 HackerGame，来打 GeekGame 了。

## †签到†

题目给了一个加密的 PDF 文件，文字无法复制。

解法有很多：

1.用在线的 [PDF 解密](https://smallpdf.com/cn/unlock-pdf)移除密码就可以正常复制出文字。

2.WPS 打开划词翻译，Ctrl+A，然后多点几次鼠标把划词翻译调出来，打开翻译窗口能更好地分辨换行。

![1](images\1.png)

3.使用 Ghostscript 进行处理~~，还是从去年选手的 WriteUp 里学来的~~。

```
$ gs -sDEVICE=txtwrite -o - prob19.pdf
GPL Ghostscript 9.56.1 (2022-04-04)
Copyright (C) 2022 Artifex Software, Inc.  All rights reserved.
This software is supplied under the GNU AGPLv3 and comes with NO WARRANTY:
see the file COPYING for details.
Processing pages 1 through 1.
Page 1
        WELCOME  ABOARD,
       ALL  PLAYERS!  GO  TO
       GEEKGAME.PKU.EDU.CN
       AND  SUBMIT  THE  FLAG:
   fa{ecm_oPUGeGmV!
   lgWloet_K_ekae2}
 别急 别急

The following warnings were encountered at least once while processing this file:
        Invalid /Length supplied in Encryption dictionary.

   **** This file had errors that were repaired or ignored.
   **** The file was produced by:
   **** >>>> Microsoft� PowerPoint� LTSC <<<<
   **** Please notify the author of the software that produced this
   **** file that it does not conform to Adobe's published PDF
   **** specification.
```

得到

```
fa{ecm_oPUGeGmV!
lgWloet_K_ekae2}
```

用了栅栏密码，丢[栅栏加密/解密](https://ctf.bugku.com/tool/railfence)栏数选择 2 解密即可。

当然也可以直接从上往下数，从左往右数看出来~~，不过比较累~~。

`flag{Welcome_to_PKU_GeekGameV2!}`

~~明年就 V3 了，什么时候 V50~~

## 小北问答 · 极速版

> 北京大学某实验室曾开发了一个叫 gStore 的数据库软件。最早描述该软件的论文的 DOI 编号是多少？

搜索 gStore 可以找到[图数据库引擎 gStore 系统](http://www.gstore.cn)。

在关于我们里提到了`2011年 gStore 相关论文首度发表 Lei Zou gStore: Answering SPARQL Queries via Subgraph Matching. PVLDB 4(8): 482-493 (2011)` 。

再把 `PVLDB 4(8): 482-493 (2011)` 拿去搜索找到对应期刊 [PVLDB: Vol 4, No 8 (acm.org)](https://dl.acm.org/toc/pvldb/2011/4/8)

就能找到 [gStore: answering SPARQL queries via subgraph matching (acm.org)](https://dl.acm.org/doi/10.14778/2002974.2002976)，根据答案格式可知是`10.14778/2002974.2002976`。![2](images\2.png)

~~好像直接搜索 `gStore doi` 就可以找到那个 doi 网站了:(~~ 

> 视频 bilibili.com/video/BV1EV411s7vu 也可以通过 bilibili.com/video/av_____ 访问。下划线内应填什么数字？

可以直接用在线[AV、BV号互转](https://bv-av.cn/get-bv-av)或者找相关代码实现，答案 `418645518`。

~~我以为 BV 号会变还找了个脚本:(~~

> 支持 WebP 图片格式的最早 Firefox 版本是多少？

这道题用必应和百度搜索`支持 WebP 图片格式的最早 Firefox 版本是多少？`都能直接告诉你是 65.0，根据格式要求，答案为 `65`。反而谷歌搜索结果不太友好，看来还是要多尝试几个搜索引擎。

> 访问网址 “http://ctf.世界一流大学.com” 时，向该主机发送的 HTTP 请求中 Host 请求头的值是什么？

其实这是域名代码(Punycode)，知道可以直接用在线工具转换。

不知道也可以按 F12，输入网址，回车，在网络请求中找到Host:`ctf.xn--4gqwbu44czhc7w9a66k.com`

> 每个 Android 软件都有唯一的包名。北京大学课外锻炼使用的最新版 PKU Runner 软件的包名是什么？

有很多种方式，可以直接[下载](https://pkunewyouth.pku.edu.cn/public/apks/pkurunner-latest.apk)用mt管理器查看包名，也可以搜索到 [pku-runner.github.io/doc.md](https://github.com/pku-runner/pku-runner.github.io/blob/android/doc/doc.md) 找到酷安上的下载地址，`apks/` 后面那串就是包名，故可得到 [`cn.edu.pku.pkurunner`](http://www.coolapk.com/apk/cn.edu.pku.pkurunner)~~虽然酷安上的下架了~~。

> 在第一届 PKU GeekGame 比赛的题目《电子游戏概论》中，通过第 6 级关卡需要多少金钱？

这题关卡级别会变，到去年的存档里找到这题，一通翻找到[libtreasure.py](https://github.com/PKU-GeekGame/geekgame-1st/blob/master/src/pygame/game/server/libtreasure.py)里有句`GOAL_OF_LEVEL = lambda level: 300+int(level**1.5)*100` 猜测就是需要的金钱数，带入公式即可。

> 我刚刚在脑海中想了一个介于 9758930138 到 9758930568 之间的质数。猜猜它是多少？

这题数字范围也会变，我是用 gmpy2.next_prime() 找下一个质数，不过要多试几次才能猜对。

> 我有一个朋友在美国，他无线路由器的 MAC 地址是 d2:94:35:21:42:43。请问他所在地的邮编是多少？

这题在给了提示才知道答案，提示在 695 Hawthorn Ave, Boulder, CO 附近，直接搜找到[695 Dellwood Ave, Boulder, CO 80304 | Zillow](https://www.zillow.com/homedetails/695-Dellwood-Ave-Boulder-CO-80304/13177176_zpid/)邮编：`80304`

然后要满分的话写个脚本就行，见 [prob01.py](src\prob01.py) 

```
flag{i-am-the-kIng-of-aNxiEtY}
flag{now-you-haVe-learnt-HoW-to-use-pwNtools}
```

