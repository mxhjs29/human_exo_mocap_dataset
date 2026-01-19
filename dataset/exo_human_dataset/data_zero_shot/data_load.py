import pickle
from pathlib import Path

root = Path(r"F:\results_save\data_zero_shot")

# 三个固定子目录名
ratio_dirs = ["agent_exo_no_assist", "agent_exo_ratio_3", "agent_exo_ratio_6"]

# mission 与 mass 的取值
mission_ids = [1, 2, 3, 5, 6, 7, 9, 10, 42]
masses = [60, 70, 80]
j =  0

all_results = []

for dirname in ratio_dirs:
    ratio_dir = root / dirname

    for mission_id in mission_ids:
        mission_dir = ratio_dir / f"mission_{mission_id}"
        if not mission_dir.exists():
            print(f"[WARN] mission dir missing: {mission_dir}")
            continue

        for mass in masses:
            mass_dir = mission_dir / f"mass_{mass}"
            if not mass_dir.exists():
                print(f"[WARN] mass dir missing: {mass_dir}")
                continue

            pkl_files = list(mass_dir.glob("*.pkl"))
            if not pkl_files:
                print(f"[INFO] no PKL in {mass_dir}")
                continue

            for pkl_file in pkl_files:
                print(f"加载: {pkl_file}  |  ratio_dir={dirname}, mission={mission_id}, mass={mass}")

                with pkl_file.open("rb") as f:
                    data = pickle.load(f)

                    j =  j + 1

print(f"\n共加载 {j} 个 pkl 文件")