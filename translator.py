from googletrans import Translator
import os
import re
import sys
import shutil
from datetime import datetime

def translate_chinese_to_bengali(text):
    try:
        translator = Translator()
        # Detect if input is Chinese
        if translator.detect(text).lang in ['zh-cn', 'zh-tw']:
            # Translate to Bengali ('bn' is language code for Bengali)
            result = translator.translate(text, src='zh-cn', dest='bn')
            return result.text
        else:
            return "Please enter Chinese text"
    except Exception as e:
        return f"Translation error: {str(e)}"

def translate_file(filepath, translator, chinese_pattern):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        chinese_texts = chinese_pattern.findall(content)
        if not chinese_texts:
            return False
            
        for chinese in chinese_texts:
            try:
                bengali = translator.translate(chinese, src='zh-cn', dest='bn').text
                content = content.replace(chinese, bengali)
            except Exception as e:
                print(f"Translation error for {chinese}: {str(e)}")
                continue
                
        # Create backup
        backup_path = f"{filepath}.bak_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(filepath, backup_path)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
        
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")
        return False

def translate_codebase_to_bengali(root_dir):
    translator = Translator()
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
    translated_files = 0
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(('.txt', '.md', '.py')):
                filepath = os.path.join(root, file)
                if translate_file(filepath, translator, chinese_pattern):
                    translated_files += 1
                    print(f"Translated: {filepath}")
    
    return translated_files

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"Starting translation in: {target_dir}")
    count = translate_codebase_to_bengali(target_dir)
    print(f"Completed! Translated {count} files.")