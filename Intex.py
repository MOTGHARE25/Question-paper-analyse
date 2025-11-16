import json
from collections import defaultdict

def analyze_papers(file_path):
    # defaultdict ka istemaal data ko aasani se store karne ke liye
    chapter_marks = defaultdict(int)
    chapter_questions = defaultdict(list)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        print("Kripya 'data.json' naam ki file usi folder mein rakhein.")
        return
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' mein JSON format galat hai.")
        return

    # Data ko process karein
    for item in data:
        chapter = item['chapter']
        marks = item['marks']
        question_info = f"Paper {item['paper_year']}, Q: {item['question_number']} ({marks} Marks)"
        
        # Har chapter ke total marks jodein
        chapter_marks[chapter] += marks
        
        # Har chapter ke questions ki list banayein
        chapter_questions[chapter].append(question_info)

    # --- Analysis Report Print Karein ---

    print("--- Question Paper Analysis Report ---")

    # 1. Sabse zyada marks wale chapters (Descending order)
    print("\n## 📈 Chapter Analysis (Marks ke Aadhar Par) ##")
    # sorted() function ka istemaal karke chapters ko marks ke hisaab se sort karein
    sorted_by_marks = sorted(chapter_marks.items(), key=lambda item: item[1], reverse=True)
    
    for chapter, marks in sorted_by_marks:
        print(f"  * {chapter}: {marks} Marks")

    # 2. Sabse zyada question wale chapters (Descending order)
    print("\n## 📊 Chapter Analysis (Questions ki Ginti ke Aadhar Par) ##")
    # Chapters ko questions ki ginti (length of list) ke hisaab se sort karein
    sorted_by_count = sorted(chapter_questions.items(), key=lambda item: len(item[1]), reverse=True)

    for chapter, questions in sorted_by_count:
        print(f"  * {chapter}: {len(questions)} Questions")

    # 3. Poori Details (Chapter-wise Question List)
    print("\n--- Sabhi Chapters ki Poori Jaankari ---")
    for chapter, questions in sorted_by_count:
        print(f"\n========================================")
        print(f"CHAPTER: {chapter}")
        print(f"TOTAL MARKS: {chapter_marks[chapter]}")
        print(f"TOTAL QUESTIONS: {len(questions)}")
        print("----------------------------------------")
        for q_info in questions:
            print(f"   -> {q_info}")
        print(f"========================================\n")

# --- Code ko Chalayein ---
# Us file ka naam dein jo aapne Step 1 mein banayi thi
analyze_papers('data.json')

