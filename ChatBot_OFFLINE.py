from sentence_transformers import SentenceTransformer, util
import tkinter as tk
from tkinter import scrolledtext


# load sentence similarity model (download 80MB model, on first run)
model = SentenceTransformer('all-MiniLM-L6-v2')

qa_pairs = [
    ("hello hi hey greetings γεια χαρά χαίρεται καλημέρα καλησπέρα", "Hi! How can I help with clothes today?"),
    ("shirt top blouse tee t-shirt", "Check out our classic cotton t-shirts or elegant silk blouses!"),
    ("pants jeans trousers shorts", "Skinny jeans or comfortable chinos work great for casual outfits!"),
    ("dress gown skirt maxi", "A flowing maxi dress is perfect for summer or evening events!"),
    ("jacket coat blazer hoodie", "A leather jacket adds style to any outfit, or try a cozy hoodie!"),
    ("shoes sneakers boots heels sandals", "White sneakers are versatile, or classic black heels for formal events!"),
    ("casual formal business wear professional", "Business casual: pair a button-up shirt with chinos or a skirt!"),
    ("winter warm sweater wool thermal", "A chunky knit sweater keeps you cozy during cold weather!"),
    ("summer light cotton breathable linen", "Linen shirts and cotton shorts are ideal for hot sunny days!"),
    ("fashion style trend outfit combination", "Layer a cardigan over a dress for a chic and versatile look!"),
    ("color size fit pattern design", "What color and size are you looking for? We have many patterns available!"),
    ("thanks thank you appreciate", "You're welcome! Need more fashion advice?"),
    ("accessories belt scarf hat tie", "A silk scarf elevates any outfit, or add a leather belt for structure!"),
    ("underwear bra socks", "Comfortable bras and quality socks are essential for any wardrobe!"),
    ("athletic sports workout gym wear", "Performance leggings and moisture-wicking shirts are great for exercise!"),
    ("elegant fancy glamorous evening", "A sequined top with tailored pants creates an elegant evening look!"),
    ("denim jean overall jumpsuit", "Denim overalls are trending and perfect for a casual cool vibe!"),
    ("polo shirt button-up oxford", "A crisp oxford shirt is timeless and works for many occasions!"),
    ("cardigan sweater pullover knit", "Layer a cardigan for warmth without losing style!"),
    ("leather suede fabric material", "Leather jackets are durable and classic, or try soft suede!"),
    ("children kids teen clothing", "Colorful t-shirts and playful patterns appeal to younger fashion fans!"),
    ("men's menswear gentleman suit", "A well-fitted suit is essential for professional and formal events!"),
    ("women's womenswear dress", "Versatile dresses work for work, casual outings, or special occasions!"),
    ("fit slim regular loose oversized", "Oversized fits are trendy, but classic slim fits never go out of style!"),
    ("cheap affordable budget budget-friendly", "Great clothes don't have to be expensive - check our clearance section!"),
    ("expensive luxury designer premium", "Luxury brands offer superior craftsmanship and timeless quality!"),
    ("sale discount offer deal", "We have up to 50% off on selected items this week!"),
    ("online store shop purchase buy", "Shop online and get free shipping on orders over $50!"),
    ("return exchange refund policy", "Easy 30-day returns - we want you to be happy with your purchase!"),
    ("delivery shipping fast quick", "Express shipping gets your order in 2-3 days!"),
    ("laundry wash care maintenance cleaning", "Use cold water for colors and hot water for whites to preserve clothing!"),
    ("iron steam press wrinkles", "Steam your clothes for a crisp look without damage!"),
    ("dry clean delicate gentle", "Delicate fabrics should be dry cleaned to maintain their quality!"),
    ("stain spot remove", "Treat stains immediately with a stain remover before washing!"),
    ("fade color bleeding prevention", "Wash new clothes separately to prevent color bleeding!"),
    ("pilling shrinkage damage", "Read care labels to avoid shrinkage and pilling!"),
    ("vintage retro classic timeless", "Vintage clothing adds unique character to any wardrobe!"),
    ("trendy modern contemporary fashion", "Current trends include oversized silhouettes and bold colors!"),
    ("eco-friendly sustainable organic", "We offer eco-friendly clothing made from organic materials!"),
    ("comfortable cozy soft snug", "Comfort is key - choose breathable fabrics for all-day wear!"),
    ("tight loose perfect fit", "A perfect fit should feel comfortable without restricting movement!"),
    ("layer layering combination mix match", "Layer a tank under a sheer top for a stylish look!"),
    ("occasion wedding party date", "A little black dress works for weddings, parties, and dates!"),
    ("weather temperature cold hot warm", "Choose layerable pieces for unpredictable weather!"),
    ("fabric cotton polyester wool silk", "Cotton is breathable, polyester is durable, wool is warm, silk is luxurious!"),
    ("pattern solid stripe plaid floral", "Stripes are classic, plaids are casual, florals are feminine!"),
    ("logo brand label name", "Premium brands offer quality assurance and timeless designs!"),
    ("style bohemian preppy grunge minimalist", "Bohemian style is free-spirited, preppy is classic, minimalist is clean!"),
    ("tattoo piercing jewelry body art", "Bold jewelry and accessories express personal style!"),
    ("makeup skincare grooming personal", "Coordinate your outfit with your makeup and grooming!"),
    ("confidence swagger presence attitude", "The best outfit is the one that makes you feel confident!"),
    ("budget planner wardrobe essentials", "Build a capsule wardrobe with versatile pieces!"),
    ("clearance liquidation inventory", "End-of-season clearance has amazing discounts!"),
    ("new arrival latest collection", "Fresh new arrivals arrive every week!"),
    ("customize tailoring alteration adjust", "We offer tailoring services for the perfect fit!"),
    ("gift present wrapping occasion", "Gift wrapping available for special occasions!"),
    ("student discount military discount senior", "We offer special discounts for students and seniors!"),
    ("loyalty rewards points membership", "Join our loyalty program and earn points with every purchase!"),
    ("subscription box monthly service", "Monthly subscription boxes deliver curated outfits to your door!"),
    ("style guide tips advice recommendation", "Our style guides help you put together perfect outfits!"),
    ("shopping assistant personal stylist", "Book a personal styling session for expert advice!"),
    ("fitting room appointment try on", "Schedule a fitting room appointment for a personalized experience!"),
    ("express yourself individual personality", "Fashion is about expressing who you are!"),
    ("seasonal collection spring summer fall", "Spring collections feature light pastels and fresh designs!"),
    ("holiday special occasion Christmas Valentine", "Holiday collections have festive colors and celebratory designs!"),
    ("workout gym fitness athletic", "Performance gear keeps you dry and comfortable during workouts!"),
    ("outdoor adventure hiking camping", "Durable outdoor wear withstands adventure and outdoor activities!"),
    ("business professional corporate office", "Corporate wear maintains professionalism in the workplace!"),
    ("casual everyday daily comfort", "Everyday casual wear should be comfortable and practical!"),
    ("pajama sleepwear loungewear", "Cozy pajamas and loungewear make staying home comfortable!"),
    ("uniform school work restaurant", "Uniforms provide consistency and professional appearance!"),
    ("costume cosplay fancy dress", "Costumes and cosplay outfits let you become your favorite character!"),
    ("rental formal dress suit", "Rent formal wear for special events without the high cost!"),
    ("made-to-order custom bespoke", "Custom-made clothes are tailored exactly to your specifications!"),
    ("vegan cruelty-free animal-free", "Our vegan clothing uses no animal products!"),
    ("fast fashion slow fashion", "Choose quality over quantity with slow fashion principles!"),
    ("thrifting second-hand used clothing", "Second-hand thrifting finds unique pieces and saves money!"),
    ("capsule wardrobe minimalist essentials", "A capsule wardrobe simplifies getting dressed daily!"),
    ("color coordination matching palette", "Coordinate colors that complement your skin tone!"),
    ("body type flattering shape silhouette", "Choose silhouettes that flatter your body type!"),
    ("petite tall average height", "We have clothing in multiple lengths for all heights!"),
    ("plus size curvy body positive", "Body-positive sizing celebrates all body types!"),
    ("sale email newsletter updates", "Subscribe to our newsletter for exclusive sales and updates!"),
    ("customer review rating testimonial", "Check customer reviews to see how others loved these items!"),
]


question_texts = [q for q, a in qa_pairs]
question_embeddings = model.encode(question_texts, convert_to_tensor=True)

THRESHOLD = 0.3


def get_response(user_input):
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = util.cos_sim(input_embedding, question_embeddings)[0]
    best_idx = similarities.argmax().item()
    best_score = similarities[best_idx].item()
    

    if best_score < THRESHOLD:
        return best_score, "Sorry, I don't understand. Can you rephrase your question about clothes?"
    
    return best_score, qa_pairs[best_idx][1]



class ChatbotUI:
    def __init__(self,root):
        self.root = root
        self.root.title("Offline Clothes Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg = "#2E2E2E")

        # Title
        tk.Label(
            root, text="Offline Clothes Chatbot", font=("Helvetica", 16, "bold"), fg = "#FFFFFF", bg="#2E2E2E"
        ).pack(pady=10)

        # Chat area (scrollable)
        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, height=20, width=50, font=("Arial", 11), bg="#3C3C3C", fg="#E0E0E0", insertbackground="white"
        )
        self.chat_area.pack(pady=10, padx=10)
        self.chat_area.insert(tk.END, "Welcome to the Offline Clothes Chatbot! Ask me anything about fashion, clothing, or style advice. \n")
        self.chat_area.config(state="disabled")

        # Input frame
        input_frame = tk.Frame(root, bg="#2E2E2E")
        input_frame.pack(pady=5)

        # Input field
        self.input_field = tk.Entry(
            input_frame, width=40, font=("Arial", 11), bg="#4A4A4A", fg="#FFFFFF", insertbackground="white"
        )
        self.input_field.pack(side=tk.LEFT, padx=5)
        self.input_field.bind("<Return>", self.send_message)

        # Send button
        tk.Button(
            input_frame, text="Send", font=("Arial", 11), bg="#4C4F50", fg="#FFFFFF", activebackground="#45A049"
        ).pack(side=tk.LEFT, padx=5)

        # Clear chat
        clear_chat_frame = tk.Frame(root, bg="#2E2E2E")
        clear_chat_frame.pack(pady=5)
        tk.Button(
            clear_chat_frame, text="Clear Chat", font=("Arial", 11), bg="#4C4F50", fg="#FFFFFF", activebackground="#BB4141"
        ).pack(padx=5)




    def send_message(self, event=None):
        user_input = self.input_field.get().strip()
        if not user_input:
            return

        score, response = get_response(user_input)
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"\nYou: {user_input}\n")
        self.chat_area.insert(tk.END, f"Match confidence: {score: .2f}\n")
        self.chat_area.insert(tk.END, f"Bot: {response}\n")
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)
        self.input_field.delete(0, tk.END)
    

    def clear_chat(self):
        self.chat_area.config(state="normal")
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.insert(tk.END, "Welcome to the Offline Clothes Chatbot! Ask me anything about fashion, clothing, or style advice. \n")
        self.chat_area.config(state="disabled")




def main():
    #download_nltk_resources()
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()