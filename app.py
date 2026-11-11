
import streamlit as st

st.set_page_config(page_title="Smart Parking Finder")

st.title("🚗 Smart Parking Finder")
st.write("Find and book available parking slots.")

if "slots" not in st.session_state:
    st.session_state.slots = {
        "P1": "Available",
        "P2": "Occupied",
        "P3": "Available",
        "P4": "Occupied"
    }

for slot, status in st.session_state.slots.items():
    st.subheader(slot)
    st.write("Status:", status)

    if status == "Available":
        if st.button("Book " + slot):
            st.session_state.slots[slot] = "Occupied"
            st.rerun()
