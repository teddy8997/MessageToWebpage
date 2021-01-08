# MessageToWebpage
    主要是將備份下來的日向坂46及櫻坂46的訂閱訊息顯示在網頁上，依照團體區分並點擊成員照片就能依照各個成員有的月份訊息顯示出來。
    要處理的檔案有mp4, txt及jpg，由於訊息為付費資訊所以不提供檔案上來。
    利用python利用檔案操作指定去遍歷資料夾下每個檔案，將有訂閱的年及月分寫到一個名為sub的EXCEL工作表中，
    並且再建立一個名為data的工作表紀錄訊息發送的日期、檔案名稱、檔案類型、檔案內容、月、及發送時間(幾點幾分)，
    最後將這個工作表使用excel2json套件轉成兩個Json格式的檔案，分別為sub.json及dada.json。
    最後在HTML中使用JavaScript讀取sub.json的資料來建立<select>年月選項給使用者選擇。選擇之後將會依據選擇的年月讀取data.json中相符的資料並且依據檔案類型來分別作處理。


# 注意事項
    由於一般主流的瀏覽器預設禁止在HTML讀取本地端的檔案也就是file access from files,如果直接執行網頁是看不到任何東西的。
    所以需要架一個http server，而自己是使用npm http-server。裝好後執行就能夠在http://127.0.0.1:8080/index.html 看到畫面

## 指令:
    $ npm install http-server -g
    $ http-server

使用技術及套件: python, HTML, CSS, JavaScript, jQuery, Json, 

