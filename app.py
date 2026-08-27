import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit 페이지 탭 설정
st.set_page_config(page_title="휴게소 통합관리 - 민원 등록", layout="centered")

# 2. HTML/CSS/JS 코드를 파이썬 문자열(변수)로 감싸기
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>휴게소 통합관리 - 민원 등록</title>
    <style>
        /* 기본 초기화 */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Noto Sans KR', 'Malgun Gothic', sans-serif;
        }
        
        body {
            background-color: #f5f6f1;
            display: flex;
            justify-content: center;
        }

        /* 모바일 컨테이너 */
        .app-container {
            width: 100%;
            max-width: 480px;
            background-color: #f5f6f1;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            position: relative;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        /* 상단 네비게이션 */
        .top-nav {
            display: flex;
            background-color: #122438;
            padding: 10px 10px 0 10px;
        }
        .top-nav div {
            flex: 1;
            text-align: center;
            padding: 12px 0;
            color: #a0aab5;
            font-size: 14px;
            font-weight: bold;
            border-radius: 20px 20px 0 0;
            cursor: pointer;
        }
        .top-nav .active {
            background-color: #f8b146;
            color: #122438;
        }

        /* 메인 헤더 */
        .main-header {
            background-color: #247543;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 20px;
        }
        .header-left {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .ic-box {
            background-color: white;
            color: #247543;
            width: 36px;
            height: 36px;
            border-radius: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: 900;
            font-size: 16px;
        }
        .header-title-group h1 {
            font-size: 18px;
            font-weight: bold;
            line-height: 1.2;
        }
        .header-title-group p {
            font-size: 12px;
            color: #d1e5d8;
        }
        .header-right {
            font-size: 14px;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        .logo-ex {
            color: #ed1c24;
            font-style: italic;
            font-weight: 900;
            font-size: 18px;
            letter-spacing: -1px;
        }
        .logo-ex span {
            color: #0072bc;
        }

        /* 메인 컨텐츠 영역 */
        .content-area {
            padding: 20px;
            flex-grow: 1;
            padding-bottom: 80px;
        }

        /* 폼 컨테이너 */
        .form-card {
            background-color: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            border: 1px solid #e0e0e0;
        }

        .section-title {
            font-size: 16px;
            font-weight: bold;
            color: #333;
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            margin-top: 5px;
        }
        .section-title::before {
            content: '';
            display: inline-block;
            width: 4px;
            height: 16px;
            background-color: #f8b146;
            margin-right: 8px;
            border-radius: 2px;
        }

        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            font-size: 14px;
            font-weight: bold;
            color: #555;
            margin-bottom: 8px;
        }

        /* 셀렉트박스 */
        select {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 15px;
            color: #333;
            appearance: none;
            background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23333' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E") no-repeat right 10px center;
            background-color: white;
            outline: none;
        }
        
        /* optgroup(그룹 제목) 스타일 */
        optgroup {
            font-weight: bold;
            color: #122438;
        }

        /* 민원 유형 버튼 */
        .type-grid {
            display: flex;
            justify-content: space-between;
            gap: 8px;
        }
        .type-btn {
            flex: 1;
            border: 1px solid #eee;
            border-radius: 8px;
            padding: 10px 0;
            background-color: white;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            gap: 5px;
            transition: all 0.2s ease;
        }
        .type-btn:active {
            transform: scale(0.95);
        }
        .type-btn.active {
            border-color: #f8b146;
            background-color: #fff9f0;
        }
        .type-icon {
            font-size: 24px;
        }
        .type-text {
            font-size: 12px;
            color: #555;
        }
        .type-btn.active .type-text {
            color: #d18f22;
            font-weight: bold;
        }

        /* 텍스트 에어리어 */
        textarea {
            width: 100%;
            height: 100px;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
            color: #333;
            resize: none;
            outline: none;
        }
        textarea::placeholder {
            color: #aaa;
        }

        /* 사진 첨부 영역 */
        .upload-section {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .upload-box {
            width: 80px;
            height: 80px;
            border: 1px dashed #999;
            border-radius: 8px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background-color: #fafafa;
            cursor: pointer;
        }
        .upload-box:active {
            background-color: #f0f0f0;
        }
        .upload-box span {
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }
        .upload-desc {
            font-size: 13px;
            color: #777;
            flex: 1;
        }

        /* 접수하기 버튼 */
        .submit-btn {
            width: 100%;
            background-color: #247543;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
            cursor: pointer;
        }
        .submit-btn:active {
            background-color: #1c5e35;
        }
        
        .notice-text {
            font-size: 12px;
            color: #777;
            margin-top: 10px;
            text-align: left;
        }

        /* 하단 네비게이션 */
        .bottom-nav {
            position: absolute;
            bottom: 0;
            width: 100%;
            background-color: #122438;
            display: flex;
            justify-content: space-around;
            padding: 10px 0;
        }
        .bottom-nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            color: #a0aab5;
            font-size: 12px;
            cursor: pointer;
            gap: 5px;
        }
        .bottom-nav-item.active {
            color: #f8b146;
        }
        .bottom-nav-icon {
            font-size: 20px;
        }
    </style>
</head>
<body>

<div class="app-container">
    
    <!-- 상단 탭 -->
    <nav class="top-nav">
        <div class="active">고객</div>
        <div>휴게소 담당자</div>
        <div>본부·지사 관리자</div>
    </nav>

    <!-- 메인 헤더 -->
    <header class="main-header">
        <div class="header-left">
            <div class="ic-box">IC</div>
            <div class="header-title-group">
                <h1>휴게소 통합관리</h1>
                <p>고객용 화면</p>
            </div>
        </div>
        <div class="header-right">
            한국도로공사 <span class="logo-ex">e<span>x</span></span>
        </div>
    </header>

    <!-- 메인 컨텐츠 영역 -->
    <main class="content-area">
        <h2 class="section-title" style="margin-bottom:10px; margin-left: 5px;">민원 등록</h2>
        
        <div class="form-card">
            
            <!-- 👉 리뉴얼된 전북본부 휴게소 목록 -->
            <div class="form-group">
                <label>휴게소 선택</label>
                <select id="restAreaSelect">
                    <optgroup label="여산휴게소">
                        <option value="여산휴게소(순천방향)">여산휴게소(순천방향)</option>
                        <option value="여산휴게소(천안방향)">여산휴게소(천안방향)</option>
                    </optgroup>
                    <optgroup label="이서휴게소">
                        <option value="이서휴게소(순천방향)">이서휴게소(순천방향)</option>
                        <option value="이서휴게소(천안방향)">이서휴게소(천안방향)</option>
                    </optgroup>
                    <optgroup label="벌곡휴게소">
                        <option value="벌곡휴게소(논산방향)">벌곡휴게소(논산방향)</option>
                        <option value="벌곡휴게소(대전방향)">벌곡휴게소(대전방향)</option>
                    </optgroup>
                    <optgroup label="서천휴게소">
                        <option value="서천휴게소(목포방향)">서천휴게소(목포방향)</option>
                        <option value="서천휴게소(서울방향)">서천휴게소(서울방향)</option>
                    </optgroup>
                    <optgroup label="군산휴게소">
                        <option value="군산휴게소(목포방향)">군산휴게소(목포방향)</option>
                        <option value="군산휴게소(서울방향)">군산휴게소(서울방향)</option>
                    </optgroup>
                    <optgroup label="대천휴게소">
                        <option value="대천휴게소(목포방향)">대천휴게소(목포방향)</option>
                        <option value="대천휴게소(서울방향)">대천휴게소(서울방향)</option>
                    </optgroup>
                    <optgroup label="홍성휴게소">
                        <option value="홍성휴게소(목포방향)">홍성휴게소(목포방향)</option>
                        <option value="홍성휴게소(서울방향)">홍성휴게소(서울방향)</option>
                    </optgroup>
                    <optgroup label="부안고려청자휴게소">
                        <option value="부안고려청자휴게소(목포방향)">부안고려청자휴게소(목포방향)</option>
                        <option value="부안고려청자휴게소(서울방향)">부안고려청자휴게소(서울방향)</option>
                    </optgroup>
                    <optgroup label="고창고인돌휴게소">
                        <option value="고창고인돌휴게소(목포방향)">고창고인돌휴게소(목포방향)</option>
                        <option value="고창고인돌휴게소(서울방향)">고창고인돌휴게소(서울방향)</option>
                    </optgroup>
                    <optgroup label="진안마이산휴게소">
                        <option value="진안마이산휴게소(익산방향)">진안마이산휴게소(익산방향)</option>
                        <option value="진안마이산휴게소(장수방향)">진안마이산휴게소(장수방향)</option>
                    </optgroup>
                    <optgroup label="금산인삼랜드휴게소">
                        <option value="금산인삼랜드휴게소(통영방향)">금산인삼랜드휴게소(통영방향)</option>
                        <option value="금산인삼랜드휴게소(대전방향)">금산인삼랜드휴게소(대전방향)</option>
                    </optgroup>
                    <optgroup label="김제휴게소">
                        <option value="김제휴게소(새만금방향)">김제휴게소(새만금방향)</option>
                        <option value="김제휴게소(전주방향)">김제휴게소(전주방향)</option>
                    </optgroup>
                    <optgroup label="정읍녹두장군휴게소">
                        <option value="정읍녹두장군휴게소(순천방향)">정읍녹두장군휴게소(순천방향)</option>
                        <option value="정읍녹두장군휴게소(천안방향)">정읍녹두장군휴게소(천안방향)</option>
                    </optgroup>
                    <optgroup label="덕유산휴게소">
                        <option value="덕유산휴게소(대전방향)">덕유산휴게소(대전방향)</option>
                        <option value="덕유산휴게소(통영방향)">덕유산휴게소(통영방향)</option>
                    </optgroup>
                    <optgroup label="익산미륵사지휴게소">
                        <option value="익산미륵사지휴게소(천안방향)">익산미륵사지휴게소(천안방향)</option>
                        <option value="익산미륵사지휴게소(순천방향)">익산미륵사지휴게소(순천방향)</option>
                    </optgroup>
                </select>
            </div>

            <!-- 민원 유형 -->
            <div class="form-group">
                <label>민원 유형</label>
                <div class="type-grid" id="typeGroup">
                    <div class="type-btn active" data-type="위생">
                        <span class="type-icon">🧼</span>
                        <span class="type-text">위생</span>
                    </div>
                    <div class="type-btn" data-type="시설">
                        <span class="type-icon">🛠️</span>
                        <span class="type-text">시설</span>
                    </div>
                    <div class="type-btn" data-type="안전">
                        <span class="type-icon">🦺</span>
                        <span class="type-text">안전</span>
                    </div>
                    <div class="type-btn" data-type="서비스">
                        <span class="type-icon">💁</span>
                        <span class="type-text">서비스</span>
                    </div>
                    <div class="type-btn" data-type="기타">
                        <span class="type-icon">❗</span>
                        <span class="type-text">기타</span>
                    </div>
                </div>
            </div>

            <!-- 민원 내용 -->
            <div class="form-group">
                <label>민원 내용</label>
                <textarea id="complaintContent" placeholder="불편사항을 자세히 적어주시면 빠르게 도와드릴게요."></textarea>
            </div>

            <!-- 사진 첨부 -->
            <div class="form-group">
                <label>사진 첨부</label>
                <div class="upload-section">
                    <div class="upload-box" onclick="alert('사진첩 접근 기능은 추후 연동됩니다.')">
                        <span>📷</span>
                        <span>사진 첨부</span>
                    </div>
                    <div class="upload-desc">
                        현장 사진이 있으면 처리 속도가 빨라져요.
                    </div>
                </div>
            </div>

            <!-- 접수하기 버튼 -->
            <button class="submit-btn" id="submitBtn">민원 접수하기</button>
            <p class="notice-text">접수 즉시 담당자에게 텔레그램으로 알림이 전송됩니다.</p>

        </div>
    </main>

    <!-- 하단 네비게이션 -->
    <nav class="bottom-nav">
        <div class="bottom-nav-item active">
            <span class="bottom-nav-icon">📝</span>
            <span>민원등록</span>
        </div>
        <div class="bottom-nav-item">
            <span class="bottom-nav-icon">🚗</span>
            <span>내 민원</span>
        </div>
        <div class="bottom-nav-item">
            <span class="bottom-nav-icon">📌</span>
            <span>공지사항</span>
        </div>
    </nav>

</div>

<!-- JS 동작 스크립트 -->
<script>
    document.addEventListener("DOMContentLoaded", function() {
        
        // 1. 민원 유형 버튼 클릭 이벤트
        const typeButtons = document.querySelectorAll('.type-btn');
        let selectedType = '위생';
        
        typeButtons.forEach(button => {
            button.addEventListener('click', function() {
                typeButtons.forEach(btn => btn.classList.remove('active'));
                this.classList.add('active');
                selectedType = this.getAttribute('data-type');
            });
        });

        // 2. 폼 제출 버튼 이벤트
        const submitBtn = document.getElementById('submitBtn');
        submitBtn.addEventListener('click', function() {
            const restArea = document.getElementById('restAreaSelect').value;
            const content = document.getElementById('complaintContent').value;
            
            if(content.trim() === '') {
                alert('민원 내용을 입력해주세요.');
            } else {
                alert('[' + restArea + ' - ' + selectedType + ' 민원]\\n텔레그램으로 성공적으로 접수되었습니다!\\n\\n내용: ' + content);
                document.getElementById('complaintContent').value = ''; // 접수 후 내용 지우기
            }
        });

    });
</script>

</body>
</html>
"""

# 3. Streamlit 화면에 HTML 렌더링
components.html(html_code, height=950, scrolling=True)
