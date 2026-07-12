
# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
## TODO


# Conda 환셩 생성 및 활성화
## TODO
if ! command -v conda &> /dev/null; then
    echo "[INFO] conda가 없어 Miniconda를 설치합니다..."
    wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -p $HOME/miniconda3
    rm ~/miniconda.sh
fi

source $HOME/miniconda3/etc/profile.d/conda.sh 2>/dev/null || source "$(conda info --base)/etc/profile.d/conda.sh"

if ! conda env list | grep -q "myenv"; then
    conda create -y -n myenv python=3.9
fi
conda activate myenv

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
## TODO
pip install --quiet mypy

# Submission 폴더 파일 실행
cd submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    problem_num=$(echo "$file" | grep -oP '(?<=_)[0-9]+(?=\.py$)')
    input_file="../input/${problem_num}_input"
    output_file="../output/${problem_num}_output"

    if [ -f "$input_file" ]; then
        python "$file" < "$input_file" > "$output_file"
    else
        python "$file" > "$output_file"
    fi
done

# mypy 테스트 실행 및 mypy_log.txt 저장
## TODO
cd ..
mypy submission/ > mypy_log.txt 2>&1

# conda.yml 파일 생성
## TODO
conda env export > conda.yml

# 가상환경 비활성화
## TODO
conda deactivate