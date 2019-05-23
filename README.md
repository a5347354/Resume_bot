# Resume_bot
> 目標：實作聊天型機器人，可以以對話方式和機器人進行溝通，機器人會將問題進行分類，並依據分類結果，回覆設定好的回話
> <br>目標架構：將面試問題進行斷詞，並訓練SVM模型，使用者輸入後，可與根據模型進行分類，最後根據分類結果，回覆設定好的對話．

## 目前功能
* 引導使用者輸入，可得到相對應的答案，可分為兩種模式（輸入"模式切換"或"切換模式"切換成不同模式）．
* 模式一-SVM模型判斷
  * 根據使用者輸入問題分成七大類（關於我、經歷、專案、獎項、論文、證照、興趣）
  * 根據類別回應相對應的訊息
* 模式二-if-in判斷
  * 根據使用者輸入的問題，包含相關字詞，則回傳相關應的訊息


## 檔案說明
* **app.py：** bot主程式
* **QAresume：** 模型副程式呼叫
* **requirements.txt：** python安裝程式清單
* **resumeQuestions.csv：** 面試問題蒐集
* **dict.txt.big：** Jieba字典
* **mode_changed：** json，bot控制目前模式的暫存
* **QAProcess.ipynb：** 建模型使用
* **vectorterms：** 建模型使用
* **cat_mapping：** 建模型使用
