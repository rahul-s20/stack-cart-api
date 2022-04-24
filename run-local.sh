

export MONGODB_URI='mongodb://localhost:27017'

export TIMEZONE='Asia/Kolkata'

echo -e "====================== Sociout by Stark ========================"
python main.py main:app --reload --host "0.0.0.0" --port 5001