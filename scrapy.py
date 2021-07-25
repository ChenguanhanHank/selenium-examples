                    for commentList in restSoup.select('div[class="rev_wrap ui_columns is-multiline"]'):
                        commenter=commentList.select('div[class="info_text pointer_cursor"]')[0].text
                        commentNum=commentList.select('span[class="badgeText"]')[0].text
                        if commentNum!="1則評論":
                            print('*****'+commenter)
                            commenterUrl='https://www.tripadvisor.com.tw/Profile/'+commenter
                            browser.get(commenterUrl)
                            commenterRes=browser.page_source
                            commenterSoup=BeautifulSoup(commenterRes, 'html.parser')
                            for otherCommentList in commenterSoup.select('div[class="nMewIgXP ui_card section"]'):
                                otherRestName=otherCommentList.select('div[class="_2ys8zX0p ui_link"]')[0].text
                                if otherRestName!=restName:
                                    commentType=otherCommentList.select('div[class="_7JBZK6_8 _20BneOSW"] span')[0]['class'][1]
                                    otherRestLocation=otherCommentList.select('div[class="_7JBZK6_8 _20BneOSW"]')[0].text
                                    otherRestRating=otherCommentList.select('div[class="_1VhUEi8g _2K4zZcBv"] span')[0]['class'][1].split('bubble_')[-1]
                                    otherCommTitle=otherCommentList.select('div[class="_3IEJ3tAK _2K4zZcBv"]')[0].text
                                    otherComment=otherCommentList.select('div[class="_133ThCYf"] q')[0].text
                                    otherRestUrl='https://www.tripadvisor.com.tw'+otherCommentList.select('div[class="_2X5tM2jP _2RdXRsdL _1gafur1D"] div a')[0]['href']
                                    with open('./otherComments/{}.txt'.format(restName), 'a', encoding='utf-8') as f:
                                        f.write('評論帳號: '+commenter+'\n')
                                        f.write('評論種類: '+commentType+'\n')
                                        f.write('餐廳名稱: '+otherRestName+'\n')
                                        f.write('餐廳位置: '+otherRestLocation+'\n')
                                        f.write('評論分數: '+str(int(otherRestRating)/10)+'\n')
                                        f.write('評論標題: '+otherCommTitle+'\n')
                                        f.write('評論內容: '+otherComment+'\n')
                                        f.write('餐廳連結: '+otherRestUrl+'\n')
                                        f.write('------'+'\n')