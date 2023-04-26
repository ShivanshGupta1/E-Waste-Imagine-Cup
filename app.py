import streamlit as st
import requests
import json
from PIL import Image

#styleing
css_style = """
<style>
    .about {
        text-align: justfiy;
        border: 2px solid black;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: justify;
    }

    .about:hover {
        box-shadow: 0px 2px 1px grey;
    }

    .grid-container {
        display: grid;
        grid-template-columns: auto auto auto;
        padding: 15px;
        column-gap: 10px;
        row-gap: 10px;
        border: 2px solid black;
        border-radius: 10px;
    }

    .img {
        width: 200px;
        height: 200px;
        margin-left: 10px;
        transition: transform 2s;
    }

    .label {
        text-align: center;
        font-weight: bold;
        margin: 0px;
    }

    .img:hover {
        transform: scale(1.1);
        
    }

    .img:hover + p {
        margin-top: 10px;
    }

</style>
"""
#set css styles
st.markdown(css_style, unsafe_allow_html=True)

#####subscription key
subscription_key = 'c537b6bc07cd411295298cb315e9ecc2'#prediction key

################################Needful Functions###################################
def get_prediction(image_data, header_data):
  #copy the URL
  url = 'https://imaginecupinstance-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/09117061-4ac4-4266-a5c4-6f3722b01216/classify/iterations/E-Waste%20Imagine%20Cup%20V1/image'
  r = requests.post(url,headers = header_data, data = image_data)
  response = json.loads(r.content)
  print(response)
  return response


#title of the web app
st.title("E Waste Classification")

#main image
st.image("https://cdnsm5-hosted.civiclive.com/UserFiles/Servers/Server_13659739/Image/recycling/banners/ewaste.jpg", caption = "E-Waste")

#sidebar
with st.sidebar:
    #set title for the sidebar
    st.header("E - Waste")
    #set the side bar image
    st.image("https://thumbs.dreamstime.com/b/pile-electronic-waste-gadgets-use-isolated-white-background-reuse-recycle-concept-144517803.jpg", caption = "Types of E-Waste")
    #about e waste
    st.subheader("What are E-Waste?")
    st.markdown("- Electronic waste or e-waste describes discarded electrical or electronic devices. Used electronics which are destined for refurbishment, reuse, resale, salvage recycling through material recovery, or disposal are also considered e-waste.")
    #bad effects of e waste
    st.subheader("Negative Effects of E-waste")
    st.markdown("- Electronic waste contains toxic components that are dangerous to human health, such as mercury, lead, cadmium, polybrominated flame retardants, barium and lithium")
    st.markdown("- The negative health effects of these toxins on humans include brain, heart, liver, kidney and skeletal system damage.")
    st.markdown("- It can also considerably affect the nervous and reproductive systems of the human body, leading to disease and birth defects.")
    st.markdown("- Improper disposal of e-waste is unbelievably dangerous to the global environment, which is why it is so important to spread awareness on this growing problem and the threatening aftermath.")
    st.subheader("How to Avoid?")
    st.markdown("- To avoid these toxic effects of e-waste, it is crucial to properly e-cycle, so that items can be recycled, refurbished, resold, or reused. The growing stream of e-waste will only worsen if not educated on the correct measures of disposal.")

tab1, tab2 = st.tabs(["About Project ❓", "Predictions 💻"])

with tab1:
    st.header("About the project")
    para = """
    <div class = "about">
        <p>
        E-waste, or electronic waste, refers to discarded electronic devices and equipment that are no longer wanted or useful. This can include items such as computers, smartphones, televisions, and other electronic appliances. E-waste is a growing problem, with millions of tons of electronic devices being discarded each year, leading to environmental and health concerns. Recycling and proper disposal of e-waste are important to reduce its negative impact on the environment and human health.
        </p>
        <ul>
            There are mainly three tabs,
            <li>About Project - You can find information and guidance on how to properly interact with the web app</li>
            <li>Predictions - This is the prediction dashboard. You can enter images to make predictions.</li>
        </ul>
    </div>
    """
    st.markdown(para, unsafe_allow_html=True)

    st.subheader("Categories Classified...")
    #categories classified
    grid_image = """
    <div class="grid-container">
        <div class="grid-item">
            <img class = "img" src = "https://checksammy.com/wp-content/uploads/2021/06/Electronics-Debrand.jpg" alt = "laptop">
            <p class = "label">Laptops</p>
        </div>
        <div class="grid-item">
            <img class = "img" src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWSXVYJ8O1YK287m-6uHZpzdNIvvKgRIrXvuJqkE-VGJ2QzjC8nqnPz96TyDHWoa3cGW8&usqp=CAU" alt = "monitor">
            <p class = "label">Monitors</p>
        </div>
        <div class="grid-item">
            <img class = "img" src = "https://images.nature.com/original/magazine-assets/nindia.2017.57/nindia.2017.57_19308654.jpg" alt = "mouse">
            <p class = "label">Mouse</p>
        </div>  
        <div class="grid-item">
            <img class = "img" src = "https://www.datocms-assets.com/27942/1607440625-pileofoldphones-compareandrecycle.jpg" alt = "mobile">
            <p class = "label">Mobile</p>
        </div>
        <div class="grid-item">
            <img class = "img" src = "https://cdn.shopify.com/s/files/1/0651/6224/8447/articles/keyboard-ewaste_1100x.jpg?v=1671645474" alt = "keyboard">
            <p class = "label">Keyboard</p>
        </div>
        <div class="grid-item">
            <img class = "img" src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-v0LD-zyf2VK5aVofb4gz_orjJw8wCnIj4A&usqp=CAU" alt = "mix">
            <p class = "label">Mix</p>
        </div> 
    </div>
    
    """

    st.markdown(grid_image, unsafe_allow_html=True)

with tab2:
   #predictions by uploading an image
    image_file = st.file_uploader("Please upload an image", accept_multiple_files=False, help="Add a supportive image type")

    if image_file:
        image = Image.open(image_file)
        image.save('input.png')

        #save the image
        st.image(image)

        with open('input.png', 'rb') as img:
            image_content = img.read()

        headers = {
            'Prediction-Key': subscription_key,
            'Content-Type': 'application/octet-stream'
        }
        response = get_prediction(image_content, headers)
        st.subheader("Label is {}".format(response['predictions'][0]['tagName']))
