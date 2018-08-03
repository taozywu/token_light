# token light （基于区块链的充值点灯应用）

这个源码是基于TrustNote 测试链的轻节点，在运行之前，需要npm install。
```
npm install
```

服务需要用到pm2，因此也要安装。

```
npm install pm2 -g
```

安装好了以后，启动RPC服务即可。

```
pm2 start rpc_service.js
```

使用python脚本获取钱包地址

```
python3 get_address.py
```

得到的是一个字符串，或一个数组。

```json
["7MMJRIOL2YRN2JSCIJVEO2QX666ZGNVZ", "SF2OZ3T4FZ4JHKGCO6DX6KMO3TYTLFTO"]
```

随便从结果中复制一个地址，这个地址就是灯的收款地址。

接下来，下载安装测试版钱包：

http://dev.trustnote.org/static/apks/wallet.apk

安装后，去 http://dev.trustnote.org/getTTT 领取测试币。



查询余额

```
python get_balance.py
```

返回类似的json字符串：

```json
{"balance": 500000000, "pending": 0, "stable": 500000000}
```


如果这个时候，从手机钱包向上面得到的地址转账，再执行这个脚本，就能发现，balance、pending和stable都会有变化。如果每隔一段时间执行，就属于自动检测灯泡的余额，以便于计算灯泡点亮时间。


balance是总额，pending是收到的数额，stable是经过验证后的数额。因为TrustNote公链对双花处理的很好，基本上pending就可以代表钱已经到了。因此，我们只需要检查pending即可。

只要执行这条命令即可：
```
python get_new_balance.py
```

现在，加一个定时器：

```
python check.py
```

这个程序2秒钟检查一次钱包余额。如果有新到的钱，则输出"on"，否则，输出"off"。

这个时候，功能已经实现了。只不过灯没有真亮，不过是用字符表示而已。现在，用树莓派可以操控gpio的：

```
python ligth.py
```

