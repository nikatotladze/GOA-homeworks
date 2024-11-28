# 3-4 


# RGB და HEX შავი და თეთრი ფერებისთვის
def color_models():
    # შავი ფერი
    black_rgb = (0, 0, 0)  # RGB შავი ფერი
    black_hex = "#000000"  # HEX შავი ფერი

    # თეთრი ფერი
    white_rgb = (255, 255, 255)  # RGB თეთრი ფერი
    white_hex = "#FFFFFF"  # HEX თეთრი ფერი

    # შედეგის გამოყოფა
    print("შავი ფერი:")
    print(f"RGB: {black_rgb}, HEX: {black_hex}")
    print("თეთრი ფერი:")
    print(f"RGB: {white_rgb}, HEX: {white_hex}")

    # ახსნა
    explanation = """
    RGB მოდელი:  
    ეს მოდელი გამოიყენება სამ ფერში - Red (წითელი), Green (მწვანე) და Blue (ლურჯი).  
    თითოეულ ფერს აქვს მნიშვნელობა 0-დან 255-მდე:
    - 0 ნიშნავს სინათლის არარსებობას (შავი)
    - 255 ნიშნავს მაქსიმალურ სინათლეს (თეთრი)

    HEX მოდელი:  
    ეს არის RGB-ის კიდევ ერთი ფორმა, მაგრამ ში-თექვსმეტობითი (hexadecimal) ფორმატში.
    თითოეული ფერის მნიშვნელობა წარმოდგენილია 2 სიმბოლოს სახით:
    - #000000 არის შავი (R=0, G=0, B=0)
    - #FFFFFF არის თეთრი (R=255, G=255, B=255)
    """
    print(explanation)

# ფუნქციის გამოძახება
color_models()


# 5

# RGB (Red, Green, Blue):

# RGB იყენებს სინათლის ინტენსივობის კომბინაციას ფერების შესაქმნელად.
# შავი ფერი (0, 0, 0) იმიტომ არის შავი, რომ არც ერთი ფერი არ ასხივებს სინათლეს.
# თეთრი ფერი (255, 255, 255) ნიშნავს მაქსიმალურ სინათლეს სამივე ფერისგან.


# HEX (Hexadecimal):

# ეს არის RGB-ის ში-თექვსმეტობითი კოდი. HEX კოდი გამოიყენება ვებ-დიზაინში.
# თითოეული ფერი (R, G, B) წარმოდგენილია 16-ობითი რიცხვით (00-დან FF-მდე).
# მაგალითად, #000000 (შავი) ნიშნავს 0 ინტენსივობას სამივე კომპონენტისთვის, ხოლო #FFFFFF (თეთრი) — მაქსიმალურს.