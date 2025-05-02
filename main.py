import csv
import time
from platforms.codeforces import get_codeforces_solved
from platforms.omegaup import get_omegaup_solved
# from platforms.atcoder import get_atcoder_solved
from platforms.codechef import get_codechef_solved

def process_csv(file_path, output_file="results.txt"):
    results = []
    header = "Name | AtCoder | CodeChef | CodeForces | AC+CC+CF | Omegaup"
    separator = "-" * len(header)

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

            atcoder_solved = 0  # get_atcoder_solved(atcoder) or 0
            codechef_solved = get_codechef_solved(codechef) or 0
            cf_solved = get_codeforces_solved(codeforces) or 0
            omegaup_solved = get_omegaup_solved(omegaup) or 0
            combined_sum = atcoder_solved + codechef_solved + cf_solved

            line = f"{name} | {atcoder_solved} | {codechef_solved} | {cf_solved} | {combined_sum} | {omegaup_solved}"
            results.append(line)
            print(f"[{i+1}] Processed: {name}")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"{header}\n{separator}\n")
        f.write("\n".join(results))

    print(f"[x] Results written to {output_file}")

if __name__ == "__main__":
    print("""
 ▄▄▄·▄▄▄        ▄▄▄▄· ▄▄▌  ▄▄▄ .• ▌ ▄ ·.    ▄▄·       ▄• ▄▌ ▐ ▄ ▄▄▄▄▄▄▄▄ .▄▄▄
▐█ ▄█▀▄ █· ▄█▀▄ ▐█ ▀█▪██•  ▀▄.▀··██ ▐███▪  ▐█ ▌▪ ▄█▀▄ █▪██▌•█▌▐█•██  ▀▄.▀·▀▄ █·
 ██▀·▐▀▀▄ ▐█▌.▐▌▐█▀▀█▄██ ▪ ▐▀▀▪▄▐█ ▌▐▌▐█·  ██ ▄▄▐█▌.▐▌█▌▐█▌▐█▐▐▌ ▐█.▪▐▀▀▪▄▐▀▀▄
▐█▪·•▐█•█▌▐█▌.▐▌██▄▪▐█▐█▌ ▄▐█▄▄▌██ ██▌▐█▌  ▐███▌▐█▌.▐▌▐█▄█▌██▐█▌ ▐█▌·▐█▄▄▌▐█•█▌
.▀   .▀  ▀ ▀█▄▀▪·▀▀▀▀ .▀▀▀  ▀▀▀ ▀▀  █▪▀▀▀  ·▀▀▀  ▀█▄▀▪ ▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀

        """)
    process_csv(input("[x] Path to CSV with usernames:\n"))
