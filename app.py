import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit 페이지 탭 설정
st.set_page_config(page_title="휴게소 통합관리시스템", layout="centered")

# 2. HTML/CSS/JS 통합 코드
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>휴게소 통합관리</title>
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

        /* 탭 내비게이션 */
        .top-nav {
            display: flex;
            background-color: #122438;
            padding: 10px 10px 0 10px;
        }
        .top-nav div {
            flex: 1;
            text-align: center;
            padding: 12px 2px;
            color: #a0aab5;
            font-size: 13px;
            font-weight: bold;
            border-radius: 20px 20px 0 0;
            cursor: pointer;
            transition: all 0.2s ease;
            white-space: nowrap;
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
        .header-title-group h1 { font-size: 18px; font-weight: bold; line-height: 1.2; }
        .header-title-group p { font-size: 12px; color: #d1e5d8; }
        
        .header-right { font-size: 14px; font-weight: bold; display: flex; align-items: center; gap: 4px; }
        .logo-ex { color: #ed1c24; font-style: italic; font-weight: 900; font-size: 18px; letter-spacing: -1px; }
        .logo-ex span { color: #0072bc; }

        /* 뷰 전환 관련 */
        .view-section { display: none; padding-bottom: 80px; flex-grow: 1; }
        .view-section.active { display: block; }
        .content-area { padding: 20px; }

        /* ============================
           [고객용] 화면 CSS
           ============================ */
        .form-card {
            background-color: white; border-radius: 12px; padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #e0e0e0;
        }
        .section-title {
            font-size: 16px; font-weight: bold; color: #333;
            display: flex; align-items: center; margin-bottom: 15px; margin-top: 5px;
        }
        .section-title::before {
            content: ''; display: inline-block; width: 4px; height: 16px;
            background-color: #f8b146; margin-right: 8px; border-radius: 2px;
        }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; font-size: 14px; font-weight: bold; color: #555; margin-bottom: 8px; }
        select {
            width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 8px;
            font-size: 15px; color: #333; appearance: none; outline: none;
            background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23333' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E") no-repeat right 10px center;
            background-color: white;
        }
        optgroup { font-weight: bold; color: #122438; }
        .type-grid { display: flex; justify-content: space-between; gap: 8px; }
        .type-btn {
            flex: 1; border: 1px solid #eee; border-radius: 8px; padding: 10px 0;
            background-color: white; display: flex; flex-direction: column;
            align-items: center; justify-content: center; cursor: pointer; gap: 5px;
        }
        .type-btn.active { border-color: #f8b146; background-color: #fff9f0; }
        .type-btn.active .type-text { color: #d18f22; font-weight: bold; }
        .type-icon { font-size: 24px; }
        .type-text { font-size: 12px; color: #555; }
        textarea {
            width: 100%; height: 100px; padding: 12px; border: 1px solid #ddd;
            border-radius: 8px; font-size: 14px; color: #333; resize: none; outline: none;
        }
        .upload-section { display: flex; align-items: center; gap: 15px; }
        .upload-box {
            width: 80px; height: 80px; border: 1px dashed #999; border-radius: 8px;
            display: flex; flex-direction: column; justify-content: center; align-items: center;
            background-color: #fafafa; cursor: pointer;
        }
        .upload-box span { font-size: 12px; color: #666; margin-top: 5px; }
        .upload-desc { font-size: 13px; color: #777; flex: 1; }
        .submit-btn {
            width: 100%; background-color: #247543; color: white; border: none;
            border-radius: 8px; padding: 15px; font-size: 16px; font-weight: bold; margin-top: 10px; cursor: pointer;
        }
        .notice-text { font-size: 12px; color: #777; margin-top: 10px; }

        /* ============================
           [담당자용] 화면 CSS
           ============================ */
        .task-card {
            background-color: white; border-radius: 12px; padding: 18px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #e0e0e0; margin-bottom: 15px;
        }
        .task-card.danger { border: 1.5px solid #ed1c24; }
        .card-header { display: flex; justify-content: space-between; align-items: center; }
        .card-title { font-size: 17px; font-weight: bold; display: flex; align-items: center; gap: 6px; color:#333; }
        .status-badge { font-size: 12px; padding: 4px 10px; border-radius: 12px; font-weight: bold; }
        .status-ing { background-color: #e6f0fa; color: #0072bc; }
        .status-wait { background-color: #fdf2e1; color: #d18f22; }
        .card-meta { font-size: 12.5px; color: #777; margin-top: 6px; }
        .card-desc { font-size: 14.5px; color: #222; margin: 12px 0; font-weight: 500; }
        .time-tag { display: inline-block; padding: 5px 12px; border-radius: 14px; font-size: 12.5px; font-weight: bold; }
        .time-safe { background-color: #edf5ef; color: #247543; }
        .time-danger { background-color: #fce8e9; color: #ed1c24; }
        .card-divider { border-top: 1px solid #eee; margin: 15px 0; }
        .action-btn { border: none; border-radius: 6px; padding: 10px 18px; font-size: 14px; font-weight: bold; cursor: pointer; }
        .btn-yellow { background-color: #f8b146; color: #122438; }
        .btn-navy { background-color: #122438; color: white; }

        /* ============================
           [본부·지사 관리자용] 대시보드 CSS
           ============================ */
        .dashboard-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 20px;
        }
        .stat-card {
            border-radius: 12px;
            padding: 18px;
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }
        .stat-card.navy { background-color: #122438; }
        .stat-card.yellow { background-color: #f8b146; color: #122438; }
        .stat-card.green { background-color: #247543; }
        .stat-card.red { background-color: #ed1c24; }
        
        .stat-num { font-size: 26px; font-weight: 900; line-height: 1.1; }
        .stat-label { font-size: 13px; font-weight: bold; margin-top: 4px; opacity: 0.9; }

        .report-card {
            background-color: white;
            border-radius: 12px;
            padding: 15px 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            border: 1px solid #e0e0e0;
        }
        .report-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid #f0f0f0;
            font-size: 14px;
        }
        .report-item:last-child { border-bottom: none; }
        .report-name { color: #333; font-weight: 500; }
        .report-val { color: #777; font-weight: bold; }
        .report-val.alert { color: #d18f22; }

        /* 하단 네비게이션 공통 */
        .bottom-nav {
            position: absolute; bottom: 0; left: 0; width: 100%;
            background-color: #122438; display: flex; justify-content: space-around; padding: 10px 0;
        }
        .bottom-nav-item {
            display: flex; flex-direction: column; align-items: center;
            color: #a0aab5; font-size: 12px; cursor: pointer; gap: 5px;
        }
        .bottom-nav-item.active { color: #f8b146; }
        .bottom-nav-icon { font-size: 20px; }
    </style>
</head>
<body>

<div class="app-container">
    
    <!-- 상단 탭 -->
    <nav class="top-nav">
        <div id="tab-customer" class="active">고객</div>
        <div id="tab-manager">휴게소 담당자</div>
        <div id="tab-admin">본부·지사 관리자</div>
    </nav>

    <!-- 메인 헤더 -->
    <header class="main-header">
        <div class="header-left">
            <div class="ic-box">IC</div>
            <div class="header-title-group">
                <h1>휴게소 통합관리</h1>
                <p id="header-subtitle">고객용 화면</p>
            </div>
        </div>
        <div class="header-right">
            한국도로공사 <span class="logo-ex">e<span>x</span></span>
        </div>
    </header>

    <!-- ==============================================
         [섹션 1] 고객용 뷰
         ============================================== -->
    <div id="view-customer" class="view-section active">
        <main class="content-area">
            <h2 class="section-title">민원 등록</h2>
            
            <div class="form-card">
                <!-- 👉 전북본부 15개 휴게소 전체 목록 반영 -->
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

                <div class="form-group">
                    <label>민원 유형</label>
                    <div class="type-grid">
                        <div class="type-btn active" data-type="위생"><span class="type-icon">🧼</span><span class="type-text">위생</span></div>
                        <div class="type-btn" data-type="시설"><span class="type-icon">🛠️</span><span class="type-text">시설</span></div>
                        <div class="type-btn" data-type="안전"><span class="type-icon">🦺</span><span class="type-text">안전</span></div>
                        <div class="type-btn" data-type="서비스"><span class="type-icon">💁</span><span class="type-text">서비스</span></div>
                        <div class="type-btn" data-type="기타"><span class="type-icon">❗</span><span class="type-text">기타</span></div>
                    </div>
                </div>

                <div class="form-group">
                    <label>민원 내용</label>
                    <textarea id="complaintContent" placeholder="불편사항을 자세히 적어주시면 빠르게 도와드릴게요."></textarea>
                </div>

                <div class="form-group">
                    <label>사진 첨부</label>
                    <div class="upload-section">
                        <div class="upload-box" onclick="alert('사진첩 접근 기능은 추후 연동됩니다.')">
                            <span>📷</span><span>사진 첨부</span>
                        </div>
                        <div class="upload-desc">현장 사진이 있으면 처리 속도가 빨라져요.</div>
                    </div>
                </div>

                <button class="submit-btn" id="submitBtn">민원 접수하기</button>
                <p class="notice-text">접수 즉시 담당자에게 텔레그램으로 알림이 전송됩니다.</p>
            </div>
        </main>

        <nav class="bottom-nav">
            <div class="bottom-nav-item active"><span class="bottom-nav-icon">📝</span><span>민원등록</span></div>
            <div class="bottom-nav-item"><span class="bottom-nav-icon">🚗</span><span>내 민원</span></div>
            <div class="bottom-nav-item"><span class="bottom-nav-icon">📌</span><span>공지사항</span></div>
        </nav>
    </div>

    <!-- ==============================================
         [섹션 2] 휴게소 담당자용 뷰
         ============================================== -->
    <div id="view-manager" class="view-section">
        <main class="content-area">
            <h2 class="section-title">신규 민원 · 처리중 (2)</h2>
            
            <div class="task-card">
                <div class="card-header">
                    <div class="card-title"><span>🛠️</span> 시설</div>
                    <div class="status-badge status-ing">처리중</div>
                </div>
                <div class="card-meta">이서휴게소(순천방향) · 2026.08.27 15:57</div>
                <div class="card-desc">화장실 세면대 물이 잘 안 내려갑니다.</div>
                <div class="time-tag time-safe">기한 24시간 중 20시간 남음</div>
                <div class="card-divider"></div>
                <button class="action-btn btn-yellow" onclick="alert('처리 완료되었습니다.')">완료 처리 등록</button>
            </div>

            <div class="task-card danger">
                <div class="card-header">
                    <div class="card-title"><span>🧼</span> 위생</div>
                    <div class="status-badge status-wait">접수</div>
                </div>
                <div class="card-meta">벌곡휴게소(논산방향) · 2026.08.27 15:57</div>
                <div class="card-desc">푸드코트 테이블에 음식물이 그대로 있어요.</div>
                <div class="time-tag time-danger">⏰ 처리 기한 4시간 초과</div>
                <div class="card-divider"></div>
                <button class="action-btn btn-navy" onclick="alert('처리를 시작합니다.')">처리 시작</button>
            </div>

            <h2 class="section-title" style="margin-top: 30px;">본부·지사 점검 요청 (1)</h2>
            <div class="task-card">
                <div class="card-header">
                    <div class="card-title">소독 실시</div>
                    <div class="status-badge status-wait">요청됨</div>
                </div>
                <div class="card-meta">이서휴게소(천안방향) · 요청: 본부 · 기한 2026-08-20</div>
                <div class="card-divider"></div>
                <button class="action-btn btn-yellow" onclick="alert('조치 완료 등록되었습니다.')">조치 완료 등록</button>
            </div>
        </main>
        
        <nav class="bottom-nav">
            <div class="bottom-nav-item active"><span class="bottom-nav-icon">📥</span><span>할일함</span></div>
            <div class="bottom-nav-item"><span class="bottom-nav-icon">✅</span><span>완료내역</span></div>
            <div class="bottom-nav-item"><span class="bottom-nav-icon">📌</span><span>공지사항</span></div>
        </nav>
    </div>

    <!-- ==============================================
         [섹션 3] 본부·지사 관리자용 뷰
         ============================================== -->
    <div id="view-admin" class="view-section">
        <main class="content-area">
            <h2 class="section-title">현장관리 대시보드</h2>
            
            <div class="dashboard-grid">
                <div class="stat-card navy">
                    <div class="stat-num">3</div>
                    <div class="stat-label">전체 민원</div>
                </div>
                <div class="stat-card yellow">
                    <div class="stat-num">1</div>
                    <div class="stat-label">처리중</div>
                </div>
                <div class="stat-card green">
                    <div class="stat-num">1</div>
                    <div class="stat-label">완료</div>
                </div>
                <div class="stat-card navy">
                    <div class="stat-num">33%</div>
                    <div class="stat-label">처리율</div>
                </div>
                <div class="stat-card red">
                    <div class="stat-num">1</div>
                    <div class="stat-label">SLA 기한 초과</div>
                </div>
                <div class="stat-card yellow">
                    <div class="stat-num">5.0 ⭐</div>
                    <div class="stat-label">평균 만족도 (1건)</div>
                </div>
            </div>

            <h2 class="section-title" style="margin-top: 30px;">휴게소별 민원 현황</h2>
            
            <div class="report-card">
                <div class="report-item"><span class="report-name">여산휴게소(순천방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">여산휴게소(천안방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">이서휴게소(순천방향)</span><span class="report-val alert">1건 · 미처리 1</span></div>
                <div class="report-item"><span class="report-name">이서휴게소(천안방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">벌곡휴게소(논산방향)</span><span class="report-val alert">1건 · 미처리 1</span></div>
                <div class="report-item"><span class="report-name">벌곡휴게소(대전방향)</span><span class="report-val">1건</span></div>
                <div class="report-item"><span class="report-name">서천휴게소(목포방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">서천휴게소(서울방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">군산휴게소(목포방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">군산휴게소(서울방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">대천휴게소(목포방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">대천휴게소(서울방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">홍성휴게소(목포방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">홍성휴게소(서울방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">부안고려청자휴게소(목포방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">부안고려청자휴게소(서울방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">고창고인돌휴게소(목포방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">고창고인돌휴게소(서울방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">진안마이산휴게소(익산방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">진안마이산휴게소(장수방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">금산인삼랜드휴게소(통영방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">금산인삼랜드휴게소(대전방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">김제휴게소(새만금방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">김제휴게소(전주방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">정읍녹두장군휴게소(순천방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">정읍녹두장군휴게소(천안방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">덕유산휴게소(대전방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">덕유산휴게소(통영방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">익산미륵사지휴게소(천안방향)</span><span class="report-val">0건</span></div>
                <div class="report-item"><span class="report-name">익산미륵사지휴게소(순천방향)</span><span class="report-val">0건</span></div>
            </div>
        </main>
        
        <nav class="bottom-nav">
            <div class="bottom-nav-item active"><span class="bottom-nav-icon">📊</span><span>대시보드</span></div>
            <div class="bottom-nav-item"><span class="bottom-nav-icon">🔍</span><span>점검요청</span></div>
            <div class="bottom-nav-item"><span class="bottom-nav-icon">📢</span><span>공지/이력</span></div>
        </nav>
    </div>

</div>

<!-- 👉 탭 전환 및 이벤트 제어 스크립트 -->
<script>
    document.addEventListener("DOMContentLoaded", function() {
        
        const tabCustomer = document.getElementById('tab-customer');
        const tabManager = document.getElementById('tab-manager');
        const tabAdmin = document.getElementById('tab-admin');
        
        const viewCustomer = document.getElementById('view-customer');
        const viewManager = document.getElementById('view-manager');
        const viewAdmin = document.getElementById('view-admin');
        
        const headerSubtitle = document.getElementById('header-subtitle');

        // 1. 고객 탭 클릭
        tabCustomer.addEventListener('click', function() {
            tabCustomer.classList.add('active');
            tabManager.classList.remove('active');
            tabAdmin.classList.remove('active');
            
            viewCustomer.classList.add('active');
            viewManager.classList.remove('active');
            viewAdmin.classList.remove('active');
            
            headerSubtitle.innerText = '고객용 화면';
        });

        // 2. 휴게소 담당자 탭 클릭
        tabManager.addEventListener('click', function() {
            tabManager.classList.add('active');
            tabCustomer.classList.remove('active');
            tabAdmin.classList.remove('active');
            
            viewManager.classList.add('active');
            viewCustomer.classList.remove('active');
            viewAdmin.classList.remove('active');
            
            headerSubtitle.innerText = '담당자용 화면';
        });

        // 3. 본부·지사 관리자 탭 클릭
        tabAdmin.addEventListener('click', function() {
            tabAdmin.classList.add('active');
            tabCustomer.classList.remove('active');
            tabManager.classList.remove('active');
            
            viewAdmin.classList.add('active');
            viewCustomer.classList.remove('active');
            viewManager.classList.remove('active');
            
            headerSubtitle.innerText = '관리자용 화면';
        });


        // --- 민원 유형 선택 및 접수 로직 ---
        const typeButtons = document.querySelectorAll('.type-btn');
        let selectedType = '위생';
        
        typeButtons.forEach(button => {
            button.addEventListener('click', function() {
                typeButtons.forEach(btn => btn.classList.remove('active'));
                this.classList.add('active');
                selectedType = this.getAttribute('data-type');
            });
        });

        const submitBtn = document.getElementById('submitBtn');
        submitBtn.addEventListener('click', function() {
            const restArea = document.getElementById('restAreaSelect').value;
            const content = document.getElementById('complaintContent').value;
            
            if(content.trim() === '') {
                alert('민원 내용을 입력해주세요.');
            } else {
                alert('[' + restArea + ' - ' + selectedType + '] 민원이 접수되었습니다!\\n내용: ' + content);
                document.getElementById('complaintContent').value = ''; 
            }
        });

    });
</script>

</body>
</html>
"""

# 3. Streamlit 화면에 HTML 렌더링 (리스트와 대시보드가 길어졌으므로 높이 1500 설정)
components.html(html_code, height=1500, scrolling=True)
