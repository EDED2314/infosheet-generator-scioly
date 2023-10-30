import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("KEY")

terms = []

with open("terms.txt", "r") as f:
    terms = f.readlines()


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {
        "role": "user",
        "content": """
Here is a fossils information sheet template that I want you to follow for each term i will give you in future questions.
Please read it, when finished say OK.

**Fossil Spotlight: Composita**

**General Details:**
- **Name:** Composita
- **Scientific Classification:** Genus Composita, Class Strophomenata
- **Geological Age:** Late Silurian to Late Permian (approximately 418 to 251 million years ago)
- **Habitat:** Marine environments worldwide
- **Fossil Type:** Brachiopod

**Description:**
Composita is a fascinating and diverse genus of brachiopods that thrived in Earth's ancient oceans for over 150 million years. This remarkable group of marine organisms is renowned for its striking fossils, which have significantly contributed to our understanding of paleontology and Earth's history.

**Distinctive Features:**
- **Symmetry:** Composita brachiopods exhibit bilateral symmetry, with two distinct shells or valves hinged together. One valve is typically larger than the other, creating a characteristic convex and concave appearance.
- **Size:** The size of Composita fossils varies widely, with some species reaching only a few millimeters while others could grow up to several centimeters in width.
- **Ornamentation:** One of the most remarkable features of Composita is its intricate shell ornamentation. The shells often display fine ribbing, spines, and various patterns, making them highly prized by collectors and researchers.

**Paleobiology:**
Composita brachiopods were filter feeders, using a lophophore, a specialized feeding organ, to capture microscopic plankton and organic particles from the water. They were an essential component of ancient marine ecosystems, providing food for other organisms and contributing to sediment formation.

**Geological Significance:**
The fossils of Composita have been instrumental in establishing the geologic history and stratigraphy of various rock formations. Their presence in sedimentary rocks serves as valuable indicators for dating and correlating geologic layers, aiding in the reconstruction of Earth's past environments.

**Distribution:**
Composita brachiopods have been discovered in various continents, including North America, Europe, Asia, and Africa. Their wide distribution helps scientists trace the movement of continents and changes in ocean basins throughout geologic time.

**Extinction:**
As the Permian period came to a close, Composita, like many other organisms, suffered a mass extinction event. This event, known as the Permian-Triassic extinction, resulted in the loss of nearly 96% of marine species, including numerous Composita species.

**Fun Facts**
fun facts about this genus/clade

**Ecology**
some facts about this species/genus interacting with its enviornment, not previously mentioned underneath other catagories

In conclusion, Composita brachiopods are a captivating and essential component of Earth's ancient history. Their fossils serve as valuable tools for geologists, paleontologists, and researchers seeking to uncover the mysteries of our planet's past. With their distinctive features, widespread distribution, and long history, Composita remains a cherished subject in the world of paleontology, shedding light on the ancient oceans and the evolution of life on Earth.
 


 """,
    },
]
count = 0
for term in terms:
    # if count >= 1:
    #     break

    term = term.replace("\n", "")

    msg = f"Please generate an info sheet based on this format for this term: {term}"

    print(msg)
    messages.append({"role": "user", "content": msg})
    response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        model="gpt-3.5-turbo",
        messages=messages,
    )
    res = response["choices"][0]["message"]["content"]
    # print(res)

    with open(f"terms/{term}.md", "w+") as f:
        f.write(res)

    messages.append({"role": "assistant", "content": res})
    # count += 1
