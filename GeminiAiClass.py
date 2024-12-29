import google.generativeai as genai

class GeminiAiClass():
    def __init__(self, apiKey: str) -> None:
        genai.configure(api_key=apiKey)
        self.model = genai.GenerativeModel("gemini-1.5-flash-8b")
    
    def correctText(self, text: str) -> str:
        inputText = f"""I'm sending to you a a text or phrase in quotation marks in brazilian portuguese. This text or phrase may or not have words that have been erroneously separated, such as "uma" transformed into "u ma" and "Alterar-se" as "Alterar -se". I need you to send me back the exact text or phrase without quotation marks or line breakers but corrected if necessary. Do not replace terms, just correct the errors mentioned. The text is: "{text}" """
        correctedText = self.model.generate_content(inputText).text
        return correctedText
    
    def finish(self) -> None:
        self.model.generate_content("It's over for now. Thank you very much for your help.")