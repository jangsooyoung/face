webcam.py : 

    python webcam.py  [gen] [box]  동영상파일 
       gen : 영상중 손 추정 위치찾아 jpg로 생성
       box : 영상중 손 추정 위치찾아 box 표시
       동영상파일 없으면 WEBCAM  
       ex) python webcam.py 
       
개발 1단계 

    0. webcam을 읽어  화면에 출력하기
    1. 동영상을 읽어 화면에 출력하기
    2. 영상을 np array로 변경하여 특정 color를 제거하거나  특정 color로 영상 보여주기 
    3. 이전 frame 새 frame변경 부분을 추적하여 box표시
    4. 영상속 특정 다각형 찾기 (손 추정 다각형, 크기) 
        - 완전 노~~가다 
    5. box 표시영역을 jpg 파일로 생성하기     
    
영상촬영 시나리오 

    1. 블루Screen 앞에서 얼굴가리고 휴대폰 통화 동작 촬영
    2. 손에 파란 장갑 끼고  휴대폰 통화 동작 촬영

    
blue 색상은 (주관적 경험이나) RGB 처리시 얼굴에 대해 확실히 대비 되는 색상입니다.