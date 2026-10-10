import os
import sqlite3
import pandas as pd
import streamlit as st

# 1. Cấu hình trang web (Tối ưu Mobile/Desktop)
st.set_page_config(
    page_title="KOSMO FALL OPEN 2026", layout="centered", page_icon="🏆"
)

# Custom CSS theo tông màu Vàng Kim & Đen/Xanh Đậm đẳng cấp theo Logo
st.markdown(
    """
    <style>
    /* Background tổng thể */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    
    /* Cấu hình Header Logo */
    .header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 10px 0 20px 0;
        text-align: center;
    }
    
    .title-text {
        font-size: 1.6rem !important;
        font-weight: 800;
        background: linear-gradient(135deg, #fef08a 0%, #eab308 50%, #ca8a04 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 10px;
        letter-spacing: 1px;
    }

    .subtitle-text {
        color: #94a3b8;
        font-size: 0.9rem;
        font-weight: 500;
    }

    /* Style cho Nút Lưu Score */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        background: linear-gradient(135deg, #eab308 0%, #ca8a04 100%);
        color: #0f172a;
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #fef08a 0%, #eab308 100%);
        color: #0f172a;
    }

    /* Style cho Expander Match Card */
    .st-emotion-cache-p5msec {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }
    
    /* Header phụ H2, H3 */
    h2, h3 {
        color: #facc15 !important;
        font-weight: 700 !important;
    }
    
    /* Bảng Xếp Hạng Style */
    .stDataFrame {
        border: 1px solid #334155;
        border-radius: 8px;
        overflow: hidden;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Header hiển thị Logo & Tiêu đề giải đấu
st.markdown('<div class="header-container">', unsafe_allow_html=True)
if os.path.exists("logo.png"):
  st.image("logo.png", width=180)
else:
  st.markdown("<h1 style='font-size: 3rem;'>🏆</h1>", unsafe_allow_html=True)

st.markdown(
    '<div class="title-text">KOSMO FALL OPEN 2026</div>', unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle-text">Giải Pickleball CLB Kosmo - Mùa Thu 2026</div>',
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# 2. Quản lý SQLite Database
DB_FILE = "pickleball_kosmo.db"


def init_db():
  conn = sqlite3.connect(DB_FILE)
  c = conn.cursor()
  c.execute("""CREATE TABLE IF NOT EXISTS matches_nam 
                 (id TEXT PRIMARY KEY, bang TEXT, team1 TEXT, team2 TEXT, score1 INTEGER, score2 INTEGER)""")
  c.execute("""CREATE TABLE IF NOT EXISTS matches_nu 
                 (id TEXT PRIMARY KEY, num INTEGER, type TEXT, nu1 TEXT, team1 TEXT, nu2 TEXT, team2 TEXT, score1 INTEGER, score2 INTEGER)""")

  # Khởi tạo bảng Nam
  c.execute("SELECT COUNT(*) FROM matches_nam")
  if c.fetchone()[0] == 0:
    nam_matches = [
        # Bảng A (6 trận)
        ("mA1", "A", "Giang - Tiền", "Tuấn - Khiêm", None, None),
        ("mA2", "A", "Tuệ - An", "Hùng - Nam", None, None),
        ("mA3", "A", "Giang - Tiền", "Tuệ - An", None, None),
        ("mA4", "A", "Tuấn - Khiêm", "Hùng - Nam", None, None),
        ("mA5", "A", "Giang - Tiền", "Hùng - Nam", None, None),
        ("mA6", "A", "Tuấn - Khiêm", "Tuệ - An", None, None),
        # Bảng B (6 trận - Đã đổi thành Huy A - Huy B)
        ("mB1", "B", "Quang Anh - Công", "Huy A - Huy B", None, None),
        ("mB2", "B", "Hà - Phượng", "Văn - Long", None, None),
        ("mB3", "B", "Quang Anh - Công", "Hà - Phượng", None, None),
        ("mB4", "B", "Huy A - Huy B", "Văn - Long", None, None),
        ("mB5", "B", "Quang Anh - Công", "Văn - Long", None, None),
        ("mB6", "B", "Huy A - Huy B", "Hà - Phượng", None, None),
        # Knockout (4 trận)
        ("bk1", "KO", "Nhất Bảng A", "Nhì Bảng B", None, None),
        ("bk2", "KO", "Nhất Bảng B", "Nhì Bảng A", None, None),
        ("t34", "KO", "Thua Bán Kết 1", "Thua Bán Kết 2", None, None),
        ("ck", "KO", "Thắng Bán Kết 1", "Thắng Bán Kết 2", None, None),
    ]
    c.executemany("INSERT INTO matches_nam VALUES (?,?,?,?,?,?)", nam_matches)

  # Khởi tạo bảng Nam Nữ
  c.execute("SELECT COUNT(*) FROM matches_nu")
  if c.fetchone()[0] == 0:
    nu_matches = [
        # 5 trận Seri Nam A
        (
            "mN1",
            1,
            "Seri A",
            "Thảo",
            "Thảo - Giang",
            "Nhiên",
            "Nhiên - Tuấn",
            None,
            None,
        ),
        (
            "mN2",
            2,
            "Seri A",
            "Hằng",
            "Hằng - Tuệ",
            "Trang",
            "Trang - Quang Anh",
            None,
            None,
        ),
        (
            "mN3",
            3,
            "Seri A",
            "Dương",
            "Dương - Huy A",
            "Thảo",
            "Thảo - Giang",
            None,
            None,
        ),
        (
            "mN4",
            4,
            "Seri A",
            "Nhiên",
            "Nhiên - Tuấn",
            "Trang",
            "Trang - Quang Anh",
            None,
            None,
        ),
        (
            "mN5",
            5,
            "Seri A",
            "Dương",
            "Dương - Huy A",
            "Hằng",
            "Hằng - Tuệ",
            None,
            None,
        ),
        # 5 trận Seri Nam B
        (
            "mN6",
            6,
            "Seri B",
            "Hằng",
            "Hằng - An",
            "Dương",
            "Dương - Huy B",
            None,
            None,
        ),
        (
            "mN7",
            7,
            "Seri B",
            "Thảo",
            "Thảo - Tiền",
            "Trang",
            "Trang - Công",
            None,
            None,
        ),
        (
            "mN8",
            8,
            "Seri B",
            "Nhiên",
            "Nhiên - Khiêm",
            "Hằng",
            "Hằng - An",
            None,
            None,
        ),
        (
            "mN9",
            9,
            "Seri B",
            "Dương",
            "Dương - Huy B",
            "Thảo",
            "Thảo - Tiền",
            None,
            None,
        ),
        (
            "mN10",
            10,
            "Seri B",
            "Trang",
            "Trang - Công",
            "Nhiên",
            "Nhiên - Khiêm",
            None,
            None,
        ),
    ]
    c.executemany(
        "INSERT INTO matches_nu VALUES (?,?,?,?,?,?,?,?,?)", nu_matches
    )

  conn.commit()
  conn.close()


init_db()


def get_matches_nam(bang):
  conn = sqlite3.connect(DB_FILE)
  df = pd.read_sql_query(f"SELECT * FROM matches_nam WHERE bang='{bang}'", conn)
  conn.close()
  return df


def get_matches_nu():
  conn = sqlite3.connect(DB_FILE)
  df = pd.read_sql_query("SELECT * FROM matches_nu ORDER BY num ASC", conn)
  conn.close()
  return df


def update_score_nam(match_id, s1, s2):
  conn = sqlite3.connect(DB_FILE)
  c = conn.cursor()
  c.execute(
      "UPDATE matches_nam SET score1=?, score2=? WHERE id=?", (s1, s2, match_id)
  )
  conn.commit()
  conn.close()


def update_score_nu(match_id, s1, s2):
  conn = sqlite3.connect(DB_FILE)
  c = conn.cursor()
  c.execute(
      "UPDATE matches_nu SET score1=?, score2=? WHERE id=?", (s1, s2, match_id)
  )
  conn.commit()
  conn.close()


def calc_bxh_nam(bang):
  df = get_matches_nam(bang)
  teams = set(df["team1"]).union(set(df["team2"]))
  stats = {
      t: {
          "Tên Đội": t,
          "Điểm": 0,
          "Thắng": 0,
          "Thua": 0,
          "Điểm Thắng": 0,
          "Điểm Thua": 0,
          "Hiệu Số": 0,
      }
      for t in teams
  }

  matches_played = 0
  for _, r in df.iterrows():
    if pd.notnull(r["score1"]) and pd.notnull(r["score2"]):
      matches_played += 1
      s1, s2 = int(r["score1"]), int(r["score2"])
      t1, t2 = r["team1"], r["team2"]
      stats[t1]["Điểm Thắng"] += s1
      stats[t1]["Điểm Thua"] += s2
      stats[t2]["Điểm Thắng"] += s2
      stats[t2]["Điểm Thua"] += s1
      if s1 > s2:
        stats[t1]["Điểm"] += 1
        stats[t1]["Thắng"] += 1
        stats[t2]["Thua"] += 1
      elif s2 > s1:
        stats[t2]["Điểm"] += 1
        stats[t2]["Thắng"] += 1
        stats[t1]["Thua"] += 1

  for t in stats:
    stats[t]["Hiệu Số"] = stats[t]["Điểm Thắng"] - stats[t]["Điểm Thua"]

  res = pd.DataFrame(list(stats.values()))
  sorted_res = res.sort_values(
      by=["Điểm", "Hiệu Số", "Điểm Thắng"], ascending=[False, False, False]
  )
  return sorted_res, matches_played


# --- GIAO DIỆN CHÍNH ---
tab1, tab2, tab3 = st.tabs(["👥 Đôi Nam", "🌺 Đôi Nam Nữ", "📊 Bảng Xếp Hạng"])

# --- TAB 1: ĐÔI NAM ---
with tab1:
  st.info(
      "📌 **Vòng bảng:** Chạm 11 (cách 2 điểm), max 15.\n📌 **Knock-out:** Chạm"
      " 15 (cách 2 điểm), max 21."
  )

  # 1. Bảng A & B
  for bang_name in ["A", "B"]:
    st.subheader(f"Bảng {bang_name}")
    df = get_matches_nam(bang_name)
    for _, row in df.iterrows():
      is_done = pd.notnull(row["score1"]) and pd.notnull(row["score2"])
      badge = "🟢 Đã xong" if is_done else "🟡 Chưa đấu"
      with st.expander(f"{row['team1']} vs {row['team2']} ({badge})"):
        col1, col2, col3 = st.columns([2, 2, 1])
        s1 = col1.number_input(
            f"Điểm {row['team1']}",
            min_value=0,
            max_value=15,
            value=int(row["score1"]) if is_done else 0,
            key=f"s1_{row['id']}",
        )
        s2 = col2.number_input(
            f"Điểm {row['team2']}",
            min_value=0,
            max_value=15,
            value=int(row["score2"]) if is_done else 0,
            key=f"s2_{row['id']}",
        )
        if col3.button("Lưu", key=f"btn_{row['id']}"):
          update_score_nam(row["id"], s1, s2)
          st.success("Đã lưu!")
          st.rerun()

  # 2. Vòng Knock-out
  st.subheader("🔴 Vòng Knock-Out (Bán kết & Chung kết)")
  bxh_a, played_a = calc_bxh_nam("A")
  bxh_b, played_b = calc_bxh_nam("B")

  if played_a < 6 or played_b < 6:
    st.warning(
        f"⏳ Vòng Bảng chưa hoàn thành ({played_a}/6 trận Bảng A, {played_b}/6"
        " trận Bảng B). Vòng Knock-out sẽ mở khi đấu đủ 12 trận vòng bảng."
    )
  else:
    nhat_a = bxh_a.iloc[0]["Tên Đội"]
    nhi_a = bxh_a.iloc[1]["Tên Đội"]
    nhat_b = bxh_b.iloc[0]["Tên Đội"]
    nhi_b = bxh_b.iloc[1]["Tên Đội"]

    df_ko = get_matches_nam("KO")

    bk1_row = df_ko[df_ko["id"] == "bk1"].iloc[0]
    bk2_row = df_ko[df_ko["id"] == "bk2"].iloc[0]

    st.markdown("### 1. Bán Kết")

    # Bán kết 1
    with st.expander(f"Bán Kết 1: {nhat_a} vs {nhi_b}"):
      col1, col2, col3 = st.columns([2, 2, 1])
      s1 = col1.number_input(
          f"Điểm {nhat_a}",
          min_value=0,
          max_value=21,
          value=(
              int(bk1_row["score1"]) if pd.notnull(bk1_row["score1"]) else 0
          ),
          key="bk1_1",
      )
      s2 = col2.number_input(
          f"Điểm {nhi_b}",
          min_value=0,
          max_value=21,
          value=(
              int(bk1_row["score2"]) if pd.notnull(bk1_row["score2"]) else 0
          ),
          key="bk1_2",
      )
      if col3.button("Lưu BK1", key="btn_bk1"):
        update_score_nam("bk1", s1, s2)
        st.success("Đã lưu Bán kết 1!")
        st.rerun()

    # Bán kết 2
    with st.expander(f"Bán Kết 2: {nhat_b} vs {nhi_a}"):
      col1, col2, col3 = st.columns([2, 2, 1])
      s1 = col1.number_input(
          f"Điểm {nhat_b}",
          min_value=0,
          max_value=21,
          value=(
              int(bk2_row["score1"]) if pd.notnull(bk2_row["score1"]) else 0
          ),
          key="bk2_1",
      )
      s2 = col2.number_input(
          f"Điểm {nhi_a}",
          min_value=0,
          max_value=21,
          value=(
              int(bk2_row["score2"]) if pd.notnull(bk2_row["score2"]) else 0
          ),
          key="bk2_2",
      )
      if col3.button("Lưu BK2", key="btn_bk2"):
        update_score_nam("bk2", s1, s2)
        st.success("Đã lưu Bán kết 2!")
        st.rerun()

    # Kiểm tra nếu hoàn thành Bán Kết -> Mở Chung kết & Tranh 3-4
    bk1_done = pd.notnull(bk1_row["score1"]) and pd.notnull(bk1_row["score2"])
    bk2_done = pd.notnull(bk2_row["score1"]) and pd.notnull(bk2_row["score2"])

    if bk1_done and bk2_done:
      if int(bk1_row["score1"]) > int(bk1_row["score2"]):
        thang_bk1, thua_bk1 = nhat_a, nhi_b
      else:
        thang_bk1, thua_bk1 = nhi_b, nhat_a

      if int(bk2_row["score2"]) > int(bk2_row["score1"]):
        thang_bk2, thua_bk2 = nhi_a, nhat_b
      else:
        thang_bk2, thua_bk2 = nhat_b, nhi_a

      st.markdown("### 2. Tranh Giải 1 - 2 - 3 - 4")

      # Tranh 3-4
      t34_row = df_ko[df_ko["id"] == "t34"].iloc[0]
      with st.expander(f"🥉 Tranh Ba - Tư: {thua_bk1} vs {thua_bk2}"):
        col1, col2, col3 = st.columns([2, 2, 1])
        s1 = col1.number_input(
            f"Điểm {thua_bk1}",
            min_value=0,
            max_value=21,
            value=(
                int(t34_row["score1"]) if pd.notnull(t34_row["score1"]) else 0
            ),
            key="t34_1",
        )
        s2 = col2.number_input(
            f"Điểm {thua_bk2}",
            min_value=0,
            max_value=21,
            value=(
                int(t34_row["score2"]) if pd.notnull(t34_row["score2"]) else 0
            ),
            key="t34_2",
        )
        if col3.button("Lưu Tranh 3-4", key="btn_t34"):
          update_score_nam("t34", s1, s2)
          st.success("Đã lưu Tranh 3-4!")
          st.rerun()

      # Chung kết
      ck_row = df_ko[df_ko["id"] == "ck"].iloc[0]
      with st.expander(f"🏆 Chung Kết: {thang_bk1} vs {thang_bk2}"):
        col1, col2, col3 = st.columns([2, 2, 1])
        s1 = col1.number_input(
            f"Điểm {thang_bk1}",
            min_value=0,
            max_value=21,
            value=int(ck_row["score1"]) if pd.notnull(ck_row["score1"]) else 0,
            key="ck_1",
        )
        s2 = col2.number_input(
            f"Điểm {thang_bk2}",
            min_value=0,
            max_value=21,
            value=int(ck_row["score2"]) if pd.notnull(ck_row["score2"]) else 0,
            key="ck_2",
        )
        if col3.button("Lưu Chung Kết", key="btn_ck"):
          update_score_nam("ck", s1, s2)
          st.success("Đã lưu Chung kết!")
          st.rerun()

# --- TAB 2: ĐÔI NAM NỮ ---
with tab2:
  st.info(
      "📌 Đấu vòng tròn 1 lượt (10 trận). Chạm 11 (cách 2 điểm), max 15.\n📌 5"
      " trận Seri Nam A đánh trước, sau đó đến 5 trận Seri Nam B."
  )
  df_nu = get_matches_nu()

  for _, row in df_nu.iterrows():
    is_done = pd.notnull(row["score1"]) and pd.notnull(row["score2"])
    badge = "🟢 Đã xong" if is_done else "🟡 Chưa đấu"
    title = (
        f"Trận {row['num']} ({row['type']}): {row['team1']} vs {row['team2']}"
        f" ({badge})"
    )
    with st.expander(title):
      col1, col2, col3 = st.columns([2, 2, 1])
      s1 = col1.number_input(
          f"Điểm {row['team1']}",
          min_value=0,
          max_value=15,
          value=int(row["score1"]) if is_done else 0,
          key=f"s1_nu_{row['id']}",
      )
      s2 = col2.number_input(
          f"Điểm {row['team2']}",
          min_value=0,
          max_value=15,
          value=int(row["score2"]) if is_done else 0,
          key=f"s2_nu_{row['id']}",
      )
      if col3.button("Lưu", key=f"btn_nu_{row['id']}"):
        update_score_nu(row["id"], s1, s2)
        st.success("Đã lưu!")
        st.rerun()

# --- TAB 3: BẢNG XẾP HẠNG ---
with tab3:
  st.subheader("🏆 Bảng Xếp Hạng Nam - Bảng A")
  bxh_a, _ = calc_bxh_nam("A")
  st.dataframe(
      bxh_a[["Tên Đội", "Điểm", "Thắng", "Thua", "Hiệu Số", "Điểm Thắng"]],
      hide_index=True,
      use_container_width=True,
  )

  st.subheader("🏆 Bảng Xếp Hạng Nam - Bảng B")
  bxh_b, _ = calc_bxh_nam("B")
  st.dataframe(
      bxh_b[["Tên Đội", "Điểm", "Thắng", "Thua", "Hiệu Số", "Điểm Thắng"]],
      hide_index=True,
      use_container_width=True,
  )

  st.subheader("🌺 Bảng Xếp Hạng Cá Nhân Nữ")
  df_nu_all = get_matches_nu()
  nu_players = ["Thảo", "Nhiên", "Hằng", "Dương", "Trang"]
  nu_stats = {
      p: {
          "VĐV Nữ": p,
          "Điểm (Thắng)": 0,
          "Thua": 0,
          "Điểm Thắng": 0,
          "Điểm Thua": 0,
          "Hiệu Số": 0,
      }
      for p in nu_players
  }

  matches_nu_count = 0
  for _, r in df_nu_all.iterrows():
    if pd.notnull(r["score1"]) and pd.notnull(r["score2"]):
      matches_nu_count += 1
      s1, s2 = int(r["score1"]), int(r["score2"])
      p1, p2 = r["nu1"], r["nu2"]
      nu_stats[p1]["Điểm Thắng"] += s1
      nu_stats[p1]["Điểm Thua"] += s2
      nu_stats[p2]["Điểm Thắng"] += s2
      nu_stats[p2]["Điểm Thua"] += s1
      if s1 > s2:
        nu_stats[p1]["Điểm (Thắng)"] += 1
        nu_stats[p2]["Thua"] += 1
      elif s2 > s1:
        nu_stats[p2]["Điểm (Thắng)"] += 1
        nu_stats[p1]["Thua"] += 1

  for p in nu_stats:
    nu_stats[p]["Hiệu Số"] = nu_stats[p]["Điểm Thắng"] - nu_stats[p]["Điểm Thua"]

  df_nu_bxh = pd.DataFrame(list(nu_stats.values())).sort_values(
      by=["Điểm (Thắng)", "Hiệu Số", "Điểm Thắng"], ascending=[False, False, False]
  )

  ranks = [
      "🥇 Nhất (Huy chương Vàng)",
      "🥈 Nhì (Huy chương Bạc)",
      "🥉 Ba (Huy chương Đồng)",
      "Hạng 4",
      "Hạng 5",
  ]
  df_nu_bxh["Danh Hiệu"] = ranks[: len(df_nu_bxh)]

  st.dataframe(
      df_nu_bxh[
          ["Danh Hiệu", "VĐV Nữ", "Điểm (Thắng)", "Thua", "Hiệu Số", "Điểm Thắng"]
      ],
      hide_index=True,
      use_container_width=True,
  )

  if matches_nu_count == 10:
    st.balloons()
    st.success(
        f"🎉 Đã hoàn thành 10/10 trận Đôi Nam Nữ! VĐV"
        f" **{df_nu_bxh.iloc[0]['VĐV Nữ']}** xuất sắc giành giải Nhất toàn đoàn!"
    )