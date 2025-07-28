# Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.
# He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let's surprise him by breaking the challenge with our python code.
# Hints to find the secret message:
# 1. The number of lines in the file tells you the meeting time.
# Note: 1<= number of lines <= 24
# If the number of lines is exceeding 12, you need to convert it to 12 hour format. For example,
# If the number of lines is 15, then the meeting time is 3 PM.
# If the number of lines is 10, then the meeting time is 10 AM.
# 2. The word appearing for the maximum number of times tells you the meeting place.

from collections import Counter

def main():
    print("Enter your text lines (press Enter on empty line to finish):")
    
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    # Determine meeting time
    line_count = len(lines)
    if line_count == 0:
        print("No lines entered.")
        return
    
    if line_count > 12:
        meeting_hour = line_count % 12
        meeting_hour = 12 if meeting_hour == 0 else meeting_hour
        meeting_time = f"{meeting_hour} PM"
    else:
        meeting_time = f"{line_count} AM"

    # Count word frequencies
    all_words = []
    for line in lines:
        words = line.strip().split()
        all_words.extend(words)

    if not all_words:
        print("No words found.")
        return

    word_counts = Counter(all_words)
    meeting_place = word_counts.most_common(1)[0][0]

    print(f"\nSecret message decoded!")
    print(f"Meeting time: {meeting_time}")
    print(f"Meeting place: {meeting_place}")

if __name__ == "__main__":
    main()
