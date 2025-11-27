from pyscript import Element

def calculate_gwa():
    # Get values from input fields
    first_name = Element("first_name").value
    last_name = Element("last_name").value

    math = float(Element("Math").value or 0)
    science = float(Element("Science").value or 0)
    english = float(Element("English").value or 0)
    history = float(Element("History").value or 0)
    pe = float(Element("PE").value or 0)

    # Calculate GWA (average of grades)
    grades = [math, science, english, history, pe]
    gwa = sum(grades) / len(grades)

    # Display the result
    Element("result").write(f"""
        <h4>Hello, {first_name} {last_name}!</h4>
        <p>Your GWA is: {gwa:.2f}</p>
    """)

