webcam.py : 

    python webcam.py  [gen] [box]  동영상파일 
       gen : 영상중 손 추정 위치찾아 jpg로 생성
       view: 영상중 손 추정 위치찾아 box 표시
       동영상파일 
       WEBCAM
       
       ex) python webcam.py 
       
개발 1단계 

    0. "python webcam.py view WEBCAM" 기능 구현하기
    1. 영상을 np array로 변경하여 특정 color를 제거하거나  color로만  영상 보여주기 
    2. 이전 frame 새 frame변경분 추적하여 box표시
    3. box 표시영역을  jpg 파일로 생성하기     
    
    
영상촬영 시나리오 

    블루Screen 앞에서 얼굴가리거 휴대폰 통화 동작 촬영
    손에 파란 장갑 끼고  휴대폰 통화 동작 촬영

    
blue 색상은 (주관적 경험이나)RGB 처리시  얼굴에 대해 확실히 대비 되는 색상입니다.