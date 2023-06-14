# 主題:AutoGPT/AgentGPT

## 簡介
此篇主要是為了研究以AI所寫出的AI執行程式,觀察其思考過程以及應用方式<br>
本來是想研究AutoGPT,但一來花錢,二來環境建置失敗,只好退而求其次以AgentGPT代替<br>
本篇所有程式碼皆為AI生成<br>


## 環境建置
如下圖,來到AgentGPT的頁面註冊後即可開始使用<br>
在下方幫AI命名並輸入想執行的指令即可<br>
<img src="https://github.com/owen4096/py2cs/blob/master/hw/agentgpt.png" width="500" height="400"  align=center /> 

## 研究內容
AgentGPT為一個讓你能在瀏覽器運行ai的一個網頁,並支援許多AI的分支功能<br>
比方說繪圖,寫作等等,且優化了使用門檻<br>
意味著以前看到的那些<咒語>使用AgentGPT或許可以不用那麼地繞口<br>
輸入你想讓AI做的事情就行了<br>
接下來以讓AI寫出八皇后問題解法的實際過程作為舉例:<br>
按下run之後ai便會上網查資料,訂定一些目標並嘗試達成<br>
<img src="https://github.com/owen4096/py2cs/blob/master/hw/agentgpt3.png" width="500" height="400"  align=center /> 
<img src="https://github.com/owen4096/py2cs/blob/master/hw/agentgpt4.png" width="400" height="400"  align=center /> 
>以上兩張圖是在不同的run下的截圖,所以目標不相同

若是無法在同一run達成所有目的(基本上都可以)<br>
那麼下一run仍會保有上一run的記憶並嘗試繼續執行以及優化解法<br>
而最後以AgentGPT寫出的8QUEEN問題解法也是沒有什麼大問題<br>
<img src="https://github.com/owen4096/py2cs/blob/master/hw/output1.png" width="500" height="400"  align=center /> 
<img src="https://github.com/owen4096/py2cs/blob/master/hw/output2.png" width="600" height="300"  align=center /> 

## 總結
本篇的靈感發想主要是來原於此影片 https://www.youtube.com/watch?v=B7bYZ5ZFbl0<br>
一個以AI寫出來的格鬥遊戲AI<br>
讓我開始思考AI到底還有多少事情能做到<br>
雖然說搬運所有AI的程式碼看起來十分偷懶<br>
但這也正是我想表達的事情<br>
AI正在不斷不斷的加強<br>
尤其是在程式的這塊<br>
我只要稍微輸入我的需求<br>
他就能自己找資料思考<br>
把我要的程式碼寫出來<br>
並且還附帶解釋<br>
我甚至動都不用動<br>
想不到有什麼辦法能不被AI取代






