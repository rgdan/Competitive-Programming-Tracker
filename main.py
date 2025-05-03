import csv
import time
from platforms.codeforces import get_codeforces_solved
from platforms.omegaup import get_omegaup_solved
from platforms.codechef import get_codechef_solved
from platforms.atcoder import get_atcoder_solved

def main(file_path, output_file="results.txt"):
    results = []
    header = "Name | AtCoder | CodeChef | CodeForces | AC+CC+CF | Omegaup"
    separator = "-" * len(header)

    atcoder_token = input("[?] Enter AtCoder token (or press Enter to skip): ").strip() or None

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:
                time.sleep(1)

            name = row["Name"]
            atcoder = row["AtCoder"]
            codechef = row["CodeChef"]
            codeforces = row["CodeForces"]
            omegaup = row["Omegaup"]

            atcoder_solved = 0
            codechef_solved = 0
            cf_solved = 0
            omegaup_solved = 0

            print(f"[{i+1}] Processing: {name}")

            if atcoder_token:
                print(f"[{i+1}.1] Processing AtCoder for {name}")
                atcoder_solved = get_atcoder_solved(atcoder, atcoder_token)
                if atcoder_solved is None:
                    atcoder_solved = 0

            print(f"[{i+1}.2] Processing CodeChef for {name}")
            codechef_solved = get_codechef_solved(codechef)

            print(f"[{i+1}.3] Processing CodeForces for {name}")
            cf_solved = get_codeforces_solved(codeforces)

            print(f"[{i+1}.4] Processing OmegaUp for {name}")
            omegaup_solved = get_omegaup_solved(omegaup)

            combined_sum = atcoder_solved + codechef_solved + cf_solved

            line = f"{name} | {atcoder_solved} | {codechef_solved} | {cf_solved} | {combined_sum} | {omegaup_solved}"
            results.append(line)


    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"{header}\n{separator}\n")
        f.write("\n".join(results))

    print(f"\n[x] Results written to {output_file}")

if __name__ == "__main__":
    print("""
 ▄▄▄·▄▄▄        ▄▄▄▄· ▄▄▌  ▄▄▄ .• ▌ ▄ ·.    ▄▄·       ▄• ▄▌ ▐ ▄ ▄▄▄▄▄▄▄▄ .▄▄▄
▐█ ▄█▀▄ █· ▄█▀▄ ▐█ ▀█▪██•  ▀▄.▀··██ ▐███▪  ▐█ ▌▪ ▄█▀▄ █▪██▌•█▌▐█•██  ▀▄.▀·▀▄ █·
 ██▀·▐▀▀▄ ▐█▌.▐▌▐█▀▀█▄██ ▪ ▐▀▀▪▄▐█ ▌▐▌▐█·  ██ ▄▄▐█▌.▐▌█▌▐█▌▐█▐▐▌ ▐█.▪▐▀▀▪▄▐▀▀▄
▐█▪·•▐█•█▌▐█▌.▐▌██▄▪▐█▐█▌ ▄▐█▄▄▌██ ██▌▐█▌  ▐███▌▐█▌.▐▌▐█▄█▌██▐█▌ ▐█▌·▐█▄▄▌▐█•█▌
.▀   .▀  ▀ ▀█▄▀▪·▀▀▀▀ .▀▀▀  ▀▀▀ ▀▀  █▪▀▀▀  ·▀▀▀  ▀█▄▀▪ ▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀
        """)
    csv_path = input("[x] Path to CSV with usernames:\n")
    main(csv_path)
