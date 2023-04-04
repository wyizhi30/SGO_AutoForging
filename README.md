# SGO自動化腳本<br>
內含"自動鍛造"及"自動狩獵"，<br>
### 自動鍛造:
> 選取要放入的素材，執行自動重複鍛造。<br>
(持續開發中，目前只能放相同素材，適合鍛垃圾刀)
### 自動狩獵:
> 自動進行戰鬥，當血量過低、體力過低、武器耐久度過低、地圖等級過高時，做出對應動作(以上條件皆可從程式碼做設定)<br>
(目前仍在開發中，條件一觸發會停止程式)

SGO網址: https://swordgale.online/

---

## 使用步驟:
1. 下載檔案(可以只下載想要的功能)<br>
2. 安裝Python (https://www.python.org/downloads/)<br>
3. 下載Webdriver (Chrome載點:https://chromedriver.chromium.org/downloads) ~~*其他瀏覽器版本自己找，記得改程式碼*~~<br>
4. 把Webdriver放到Python安裝目錄 or 跟此程式放在同個資料夾<br>
5. CMD安裝Selenium (指令:pip install selenium)<br>
6. CMD執行程式(EX:python SGO_Forging.py)<br>

---

## 參考資料
### Selenium 網頁自動化操作:
* [動態網頁爬蟲第一道鎖— Selenium教學：如何使用Webdriver](https://northbei.medium.com/%E5%9C%A8windows%E4%B8%8A%E5%AE%89%E8%A3%9Dpython-selenium-%E7%B0%A1%E6%98%93%E6%95%99%E5%AD%B8-eade1cd2d12d)<br>
* [【Day 18】動態網頁爬蟲-Selenium（1/2） - iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10301898)<br>
* [Selenium 函式庫- Python 網路爬蟲教學 - STEAM 教育學習網](https://steam.oxxostudio.tw/category/python/spider/selenium.html)<br>
### GitHub README撰寫:
* [所有關於README.md 文件標記 - GitHub - by BEPb](https://github.com/BEPb/README/blob/master/README.chinese.md) (超推，工具書等級!!)
* [GitHub上README.md排版样式教程_md文件排版_本性的博客](https://blog.csdn.net/u012067966/article/details/50736647)<br>
* [基本撰写和格式语法- GitHub 文档](https://docs.github.com/zh/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#paragraphs)<br>
