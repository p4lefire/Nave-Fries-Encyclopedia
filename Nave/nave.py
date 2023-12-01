import streamlit as st
import os
st.set_page_config(
    page_title="North Ave Fries Encyclopedia",
    page_icon="🍟"
    )
st.sidebar.title("North Ave Fries Encyclopedia")
bunkChoice = st.sidebar.radio(
    "Pick a bunk for a curated, top-notch, completely arbitrary selection of fries based on your bunk preference (and nothing else whatsoever)!",
      ["Top", "Bottom", "I switch around", "I don't bunk"])#NEW (1), 1st input method
st.sidebar.header("Key:")
st.sidebar.write("**Description:** A brief description and/or evaluation of each fry.")
st.sidebar.write("**Rarity:** How common are these fries at North Ave Dining Hall?")
st.sidebar.write("**Needs Condiments:** Does this fry stand on its own without condiments? Not necessarily an indicator of quality, but a useful piece of information to know regardless.")
st.sidebar.write("**Overall rating:** The fry's overall rating out of 10, where 10 is the best/highest rating.")

def landingPage(bunk):
    st.title(bunk + " Fries") #NEW (2)
    st.write("Here are all the fries for your bunk preference! Now, pick a type of fry to learn more about!")
    st.write("Disclaimer: This encyclopedia does not contain all the fries served at North Ave Dining Hall.")
    if bunk == "Top": 
      friesList = ["Loaded fries", "Steak fries", "Sidewinders", "Battered fries"]
      topSelection = st.selectbox("Select one:", friesList) #NEW (3), 2nd input method

      if topSelection == "Loaded fries":
        st.image("images/loaded.jpeg", use_column_width=True)
        st.header("Description:")
        st.write("A type of fry with many flavors and ingredients. Truly, a treasure of North Ave Dining Hall.")
        st.subheader("Rarity: Very rare")
        st.subheader("Needs condiments: No")
        st.subheader("Overall rating: 10/10")

      elif topSelection == "Steak fries":
        st.image("images/steak.jpg", use_column_width=True)
        st.header("Description:")
        st.write("A fry rather lacking in flavor compared to many of its counterparts, although you will find many variations of it at North Ave Dining Hall. Less crispy than many other fries such as sidewinders, waffle fries, and battered fries.")
        st.subheader("Rarity: Common")
        st.subheader("Needs condiments: Yes")
        st.subheader("Overall rating: 8/10")

      elif topSelection == "Sidewinders":
        st.image("images/sidewinder.jpg", use_column_width=True)  
        st.header("Description:")
        st.write("Undoubtedly one of the best fries at North Ave Dining Hall. Often slightly undercooked and not as crispy as it could be but delicious regardless. The type of fry you would go back to get an entire plate of seconds for.")
        st.subheader("Rarity: Common")
        st.subheader("Needs condiments: No")
        st.subheader("Overall rating: 10/10")       

      elif topSelection == "Battered fries":
        st.image("images/battered.jpg", use_column_width=True)
        st.header("Description:")
        st.write("Some of the very best fries you can ever get at North Ave Dining Hall, if not the very best. Crispy, flavorful, and even better with condiments, although it doesn't need them. 10/10 would get an entire plate of seconds. Battered fries have it all!")
        st.subheader("Rarity: Rare")
        st.subheader("Needs condiments: No")
        st.subheader("Overall rating: 10/10")

  #------------------------------------------------------------------------------------------
    elif bunk == "Bottom":
      friesList = ["Shoestring fries", "Curly fries"]
      bottomSelection = st.selectbox("Select one:", friesList)

      if bottomSelection == "Shoestring fries":
        st.image("images/shoestring.jpg", use_column_width=True)
        st.header("Description:")
        st.write("A flavorless, lacking fry. Not crispy whatsoever. Commonly served at West Village Dining Hall, which should tell you all you need to know about them.")
        st.subheader("Rarity: Common")
        st.subheader("Needs condiments: Yes")
        st.subheader("Overall rating: 5/10")

      elif bottomSelection == "Curly fries":
        st.image("images/curly.jpg", use_column_width=True)
        st.header("Description:")
        st.write("A fairly good fry. Not as good as sidewinders and battered fries, but a solid option.")
        st.subheader("Rarity: Very rare")
        st.subheader("Needs condiments: No")
        st.subheader("Overall rating: 8/10")        
#------------------------------------------------------------------------------------------
    elif bunk == "Switch":
      friesList = ["Sweet potato fries", "Waffle fries"]
      switchSelection = st.selectbox("Select one:", friesList)
    
      if switchSelection == "Sweet potato fries":
        st.image("images/sweetpotato.jpg", use_column_width=True)
        st.header("Description:")
        st.write("A fry that's rather hit-or-miss. Usually an unexpected surprise, but a decent fry depending on how well it's cooked.")
        st.subheader("Rarity: Uncommon")
        st.subheader("Needs condiments: No")
        st.subheader("Overall rating: 7/10")  

      elif switchSelection == "Waffle fries":
        st.image("images/waffle.jpg", use_column_width=True)
        st.header("Description:")
        st.write("A fry that calls to mind a certain place in the Student Center. No, not DePoe Eye Center... A certain fast food chicken chain! Though these fries aren't as good as that chain's, they're still a welcome visitor at the North Ave Dining Hall fry section.")
        st.subheader("Rarity: Common")
        st.subheader("Needs condiments: No")
        st.subheader("Overall rating: 9/10")        
#------------------------------------------------------------------------------------------
    elif bunk == "Non":
      friesList = ["Potato wedges", "Tater tots"]
      nonSelection = st.selectbox("Select one:", friesList)

      if nonSelection == "Potato wedges":
        st.image("images/wedge.jpg", use_column_width=True)
        st.header("Description:")
        st.write("Not a fry, but still a decent choice. If you're not up for any fried potatoes, these are a solid option.")
        st.subheader("Rarity: Common")
        st.subheader("Needs condiments: No")
        st.subheader("Overall rating: 8/10")  

      elif nonSelection == "Tater tots":
        st.image("images/tater.jpg", use_column_width=True)
        st.header("Description:")
        st.write("A \"fry\" that is rather unpleasant to see any time outside breakfast hours. The type of horror and rage you feel when you expect fries for lunch and/or dinner and find tater tots instead is truly unmatched.")
        st.subheader("Rarity: Common")
        st.subheader("Needs condiments: No")
        st.subheader("Overall rating: 2/10")  

if bunkChoice == "Top":
    landingPage(bunkChoice)

elif bunkChoice == "Bottom":
    landingPage(bunkChoice)

elif bunkChoice == "I switch around":
    landingPage("Switch")

elif bunkChoice == "I don't bunk":
    landingPage("Non")