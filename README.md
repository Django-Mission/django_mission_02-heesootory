# Django mission2 - advanced

### ✍️ modeling

![image1](/Image/mission2.PNG)
![image1](/Image/mission2_1.PNG)

### <mark>Inquiry class</mark>

* category : CharField(최대길이 지정 필수)
    - 최대길이 10
    - choices으로 선택지 내려오는 옵션 구성. cate 튜플 참조
    - null은 default로 필수요소.
* subject : CharField
    - 최대길이 50
* email : EmailField
    - 최대 길이 254
    - null = True -> NULL(정보없음) 가능 -> 필수 요소 X.
    - blank = True -> 빈 문자열 가능
* email_receive : BooleanField (체크박스)
    - default = False : 기본값 체크 X
* message : CharField
    - 최대길이 500
    - null = True -> NULL(정보없음) 가능 -> 필수 요소 X.
    - blank = True -> 빈 문자열 가능
* message_receive : BooleanField
* content : TextField
    - null, blank 없음 -> 공백이나, NULL 불가 -> 필수요소
* Image : ImageField
    - null = True -> NULL(정보없음) 가능 -> 필수 요소 X.
    - blank = True -> 빈 문자열 가능

<br>

### <mark>Answer class</mark>
* content : TextField
* reference : URLField
    - null = True -> NULL(정보없음) 가능 -> 필수 요소 X.
    - blank = True -> 빈 문자열 가능
* create_date : DateTimeField
    - auto_now_add = True -> 생성일자 자동으로 받아옴
* final_modify_date : DateTimeField
    - auto_now = True -> 수정일자 자동으로 받아옴.
* final_modifier : CharField
    - 최대길이 20
    - null = True -> NULL(정보없음) 가능 -> 필수 요소 X.
    - blank = True -> 빈 문자열 가능
* writer : ForeignKey
    - 작성자와 답변의 관계는 1 : N의 관계 이므로, N에 해당하는 답변이 ForeignKey를 가짐.
* inquiry : ForeignKey
     - 작성자와 답변의 관계는 1 : N의 관계 이므로, N에 해당하는 답변이 ForeignKey를 가짐.



