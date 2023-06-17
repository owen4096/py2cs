# 主題:人工智慧的大腦 卷積神經網路(CNN)與多層感知機(MLP) 研究筆記

## 前言
為什麼會想選這個主題? 因為我對於人工智慧現今的成就感到很好奇<br>
為什麼它們可以做到近似於人類的思考邏輯?How?And why?<br>
在我以前對深度學習部分AI的認知就是AI鬼抓人遊戲<br>
如下圖<br>
<img src="https://github.com/owen4096/py2cs/blob/master/hw/ai1.png" width="700" height="400"  align=center /> <br>
此遊戲簡單來說就是人要躲鬼,在多次嘗試會發現箱子可以阻擋鬼,而鬼也會在之後發現梯子可以越過牆<br>
就是通過不斷的run 不斷的train 利用加分扣分控制AI,驅使它往高分移動,有點類似爬山演算法的概念<br>
但後來在某次的研究中發現其並不完全適用所有場合<br>
比方說貪吃蛇<br>
又比方說格鬥遊戲AI<br>
先以貪吃蛇為例子,假設以吃果子加分,撞自己扣分<br>
這麼簡單的獎懲機制會導致蛇繞著自己自轉<br>
因為太容易撞到自己,太不容易吃到果子了<br>
格鬥遊戲也是同理<br>
而這結果是我當初沒有想過的,促使我對AI的思考邏輯產生興趣,想要從根部了解這種深度學習AI的思維,也就有了這篇研究筆記<br>


## 多重感知機(MLP) 
要說到這種跟Neural Network(NN),也就是神經原網路有關的東西,肯定要先從最基本的開始說<br>
所謂NN,就是含有輸入,隱藏,輸出三層的神經網路<br>
<img src="https://github.com/owen4096/py2cs/blob/master/hw/ai2.png" width="700" height="400"  align=center /> <br>
顧名思義,輸入負責輸入訊號,隱藏負責計算,輸出負責輸出信號<br>
而MLP就是將輸入以各式各樣的數學函數及參數權重進行計算,比如說梯度下降,反傳遞等等<br>
以遵循人類神經的方式去學習並預測數據,更改參數使預設值更接近實際值<br>

## 卷積神經網路(CNN) 
卷積神經網路則是以MLP為基底,增加了池化層(pooling)以及卷積層(kernals/Convolution Layer)<br>
- 卷積層
所謂的卷積層主要是因為Neural Network中,因為是以fully connect(全連通)的方式連接的<br>
這樣的好處是傳輸的彈性大,但也會導致每一層的權重(weight)太高<br>
但其實不用每個Neural都需要分析整張圖片,藉由分析局部以及分享參數的方式降低每個Neural的權重<br>
利用了步長(strides)以及填充(padding)控制卷積核(kernel)以滑動的方式提取input信息<br>
使其決定每一個小區域的特徵接受域(Receptive field)<br>
雖然降低了彈性,但也相對的讓每個Neural降低了負擔<br>

- 池化層
池化層的主要目的為將整個input做subsampling<br>
將被共用同一組參數的--filter(也就是kernel/卷積核) 做完卷積層的行為之後<br>
以自訂義的方式(根據個人經驗,資料等制定出的規則)將input做局部取最大,最小,平均等<br>
將input的運算量縮小,減少算力消耗<br>
但現在科技日漸進步,越來越多不這樣做了<br>
因為此方式多少會有對input失真的情況,出現誤差<br>
而現今電腦算力能夠負荷沒有subsampling的input<br>
因此也有許多模型將此層抽掉<br>
下圖為CNN模型<br>
<img src="https://github.com/owen4096/py2cs/blob/master/hw/ai3.png" width="700" height="400"  align=center /> 




# 參考文獻
陳鍾誠老師的上課教材<br>
- youtube     : https://www.youtube.com/@ccckmit <br>
- github教材  : https://github.com/ccc111b/py2cs <br>
深度學習 :CNN原理 https://cinnamonaitaiwan.medium.com/%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92-cnn%E5%8E%9F%E7%90%86-keras%E5%AF%A6%E7%8F%BE-432fd9ea4935<br>
李弘毅教授的投影片及影片解析 : https://www.youtube.com/watch?v=OP5HcXJg2Aw&ab_channel=Hung-yiLee <br>
神經網路模型有哪些？種類與使用介紹(MLP/CNN) https://ithelp.ithome.com.tw/articles/10303535 <br>


