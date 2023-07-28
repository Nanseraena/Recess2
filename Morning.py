# EXERCISE: Write a program to ask students about their mental health
# Prompt students on a scale of 1 to 10 to rate their mental health.

Mental_health = {
    1: "You need to see a mental doctor ",
    2: " you need reherb  ",
    3: " Go for therapy, you are depressed ",
    4: " Have you thoughht about seeing a doctor or going for therapy",
    5: " Stop overthinking and try to exercise",
    6: " Start taking a walk to release your emotions ",
    7: " You are fine, you just need new hobbies to take away your stress ",
    8: "You are doing great you do not need medical help ",
    9: " Prefect you are doing great with your life",
    10: "You are healthy ,you have high emotional intelligence"
}
rate = int(input("On a scale of 1 to 10, how are you feeling? "))

if rate in Mental_health :
    print(Mental_health[rate]) 