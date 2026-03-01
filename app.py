import streamlit as st
import os
from dotenv import load_dotenv
from zhipuai import ZhipuAI

load_dotenv()


st.set_page_config(
    page_title="MU MA English",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


SYLLABUS_DATA = {
    "Semester I": {
        "Paper I: English Poetry (PAENG101)": {
            "Unit 1: Chaucer to Metaphysical (1340-1660)": {
                "texts": [
                    "Geoffrey Chaucer: Prologue to the Canterbury Tales",
                    "Edmund Spenser: The Faerie Queene (Book 1, Canto 1-2)"
                ],
                "reference": """
                **Socio-cultural/Political:** Feudalism and Social Status; Ecclesiastical/Church Control; Printing and Literacy; Travel and Exploration under Tudor reign and Early Stuarts; English Civil War and Puritan Regime.
                **Forms/Genres/Movements:** Renaissance, Humanism, Reformation, Allegory, Songs, Sonnets and Sonnet Sequence, Lyrics, Metaphysical poetry, Cavalier poetry.
                **Representative Poets:** Geoffrey Chaucer, William Langland, Wyatt & Surrey, Philip Sidney, Edmund Spenser, William Shakespeare, Ben Jonson, John Donne, Andrew Marvell, George Herbert, Richard Crashaw, Henry Vaughan, Robert Herrick, Thomas Carew, Sir John Suckling, Richard Lovelace.
                """
            },
            "Unit 2: Milton to Age of Transition (1661-1798)": {
                "texts": [
                    "John Milton: Paradise Lost, Book 9",
                    "Alexander Pope: The Rape of the Lock"
                ],
                "reference": """
                **Socio-cultural/Political:** Restoration, Rise of Party Politics, Glorious Revolution, Age of Satire.
                **Forms/Genres/Movements:** Neo-Classicism, Epic, Satire, Mock Epic, Lyrics.
                **Representative Poets:** John Milton, John Bunyan, John Dryden, Alexander Pope, Jonathan Swift, Oliver Goldsmith, William Collins, Thomas Gray.
                """
            },
            "Unit 3: Romantic Revival to Pre-Raphaelite (1798-1901)": {
                "texts": [
                    "William Wordsworth: ‘Tintern Abbey’, ‘London, 1802’, ‘The World is too much with Us’",
                    "Alfred Lord Tennyson: ‘The Two Voices’, ‘Locksley Hall’, ‘The Lotus-Eaters’"
                ],
                "reference": """
                **Socio-cultural/Political:** Revival of Romanticism of Elizabethan Age; Impact of Industrial Revolution; French Revolution; Influence of German Philosophy (Schiller and Kant); Romanticism as a reaction to Neoclassicism; Romantic concept of imagination, Sublime, Exoticism, Romantic notion of nature; Victorian age literary characteristics; Darwinism; Age of Science; Age of Faith and Doubt (Victorian Dilemma); Victorian compromise and conservatism; Victorian concept of morality.
                **Forms/Genres/Movements:** Aesthetic Movement, Pre-Raphaelite Movement, Pantheism, Medievalism, Lyric, Sonnet, Ballad, Ode, Dramatic Monologue.
                **Representative Poets:** William Blake, Robert Southey, William Wordsworth, S.T. Coleridge, Lord Byron, P.B. Shelley, John Keats, Elizabeth Barrett Browning, Alfred Lord Tennyson, Robert Browning, Matthew Arnold, Thomas Hardy, D.G. Rossetti, Christina Rossetti, William Morris, A.C. Swinburne, G.M. Hopkins.
                """
            },
            "Unit 4: Modernism and After": {
                "texts": [
                    "T. S Eliot: ‘The Hollow Men’, ‘Ash Wednesday’",
                    "Philip Larkin: ‘Afternoons’, ‘Essential Beauty’, ‘Mr. Bleany’",
                    "Craig Raine: ‘An Inquiry into Two Inches of Ivory’, ‘The Onion, Memory’"
                ],
                "reference": """
                **Socio-cultural/Political:** Influence of Science, Technology and Psychology; World War I & II and Interwar Period; Marxist Ideology and influence of Russian Experiment; Post-World War II developments.
                **Trends and Movements:** Georgian Poetry, Free Verse, Modernism, Symbolism, Cubism, Imagism, Dadaism, Surrealism, Neo-Romanticism, The Movement, Postmodernism and Meta Modernism.
                **Representative Poets:** W. B. Yeats, Wilfred Owen, W. H. Auden, Stephen Spender, Louise Bennett, Philip Larkin, Donald Davie, Ted Hughes, Carol Ann Duffy, Craig Raine, Roy Fuller, Dylan Thomas, Geoffrey Hill.
                """
            }
        },
        "Paper II: Non-Fictional Prose (PAENG102)": {
            "Unit 1: Letters & Diaries": {
                "texts": [
                    "Letters: Elizabeth I / Charles I / Pope & Wycherley / Katherine Mansfield",
                    "Diaries: Dorothy Wordsworth / Anne Frank"
                ],
                "reference": """
                **Background:** Socio-cultural, political and intellectual currents shaping letters and diaries. Interplay of personal, intellectual and social.
                **Forms:** Different types of letters and forms of diaries, prose styles. Letters from royal family (Elizabeth I onwards), eminent writers (Pope, Wycherley, Blake, Wordsworth, Coleridge, Lamb, Dickens, Bronte, Mansfield, Lawrence).
                **Diaries:** Samuel Pepys, war captains, George Orwell, W. N. P. Barbellion.
                """
            },
            "Unit 2: Essays and Histories": {
                "texts": [
                    "Essays: Francis Bacon / R. L. Stevenson / G. B. Shaw",
                    "Histories: Hibbert (1857 Mutiny) / E. P. Thompson (Working Class)"
                ],
                "reference": """
                **Background:** Socio-cultural currents shaping essays and histories. Interplay of personal and political.
                **Forms:** 17th-century essays (genteel behaviour), 19th-century (critique of society/religion/education), 20th-century (literary/cultural/political criticism).
                **History Genres:** Political, diplomatic, cultural, social, economic, philosophical, psychoanalytical.
                **Representatives:** Bacon, Burton, Milton, Hobbes, Swift, Johnson, Goldsmith, Lamb, Hazlitt, Carlyle, Arnold, Stevenson, Butler, Gardiner, Chesterton, Lucas, Eliot, Woolf, Shaw, Wells, Huxley. Voltaire, Gibbon, Trevelyan, Thompson, Skinner, Laslett, Russell.
                """
            },
            "Unit 3: Travelogues & Biographies": {
                "texts": [
                    "Travelogue: Evelyn Waugh (Remote People)",
                    "Biography: James Boswell (Life of Samuel Johnson)"
                ],
                "reference": """
                **Background:** Discovery of trade routes, curiosity re: new lands, industrialization, revolution in publishing/locomotion, rise in literacy. Travel/biography association with class and leisure.
                **Travel Writing:** Historical info, sociological/anthropological observations, rise during interwar years.
                **Biography:** Intersection of history, archival study, public persona vs private accounts. Rise of celebrity culture.
                **Representatives:** Hakluyt, Cook, Boswell, Darwin, Stevenson, Greene, Byron, West, Fleming, Waugh. Strachey, Graves, Churchill, Milford.
                """
            },
            "Unit 4: Speeches & Periodicals": {
                "texts": [
                    "Speeches: Churchill / Thatcher",
                    "Periodicals: Addison (Spectator 45) / Steele (Spectator 49)"
                ],
                "reference": """
                **Background:** Rise of periodicals (18th century), importance of Addison/Steele as topical reflections. Demand for entertainment with rising middle/working classes. 20th-century changes (advertising, illustrations, mass-market).
                **Speeches:** Stylistic devices, gestures, oratory. Speeches as mass address/propaganda (TV/Social Media).
                **Evolution:** Addison, Steele, Swift -> e-periodicals. Oratory of Macaulay, Gladstone, Sheridan, Burke, Fox, Churchill.
                """
            }
        },
        "Paper III: Literary Criticism (PAENG103)": {
            "Unit 1: Classical Criticism": {
                "texts": [
                    "Aristotle: Poetics (Chapters 1 to 15)",
                    "Longinus: On the Sublime (Chapters 1 to 8)"
                ],
                "reference": """
                **Terms/Concepts:** Horace’s views on poetry; Plato and Gosson’s attack on poetry; Three Unities; Mimesis; Catharsis; Hamartia; Peripeteia; Anagnorisis; Six elements of tragedy; Notion of the Sublime; Five Sources of Sublimity; Sir Philip Sidney’s views.
                """
            },
            "Unit 2: Neoclassical Criticism": {
                "texts": [
                    "John Dryden: Essay on Dramatic Poesy",
                    "Dr. Samuel Johnson: Preface to Shakespeare"
                ],
                "reference": """
                **Terms/Concepts:** Alexander Pope’s ‘Essay on Criticism’; Relative merits of classical vs modern drama; Comparison of French vs English drama; Dr Johnson’s ‘Lives of the Poets’.
                """
            },
            "Unit 3: Romantic & Victorian Criticism": {
                "texts": [
                    "S.T. Coleridge: Biographia Literaria (Ch IV, XIII, XIV)",
                    "Matthew Arnold: “The Function of Criticism at the Present Time”"
                ],
                "reference": """
                **Terms/Concepts:** Causes of rise of Romantic Criticism; Features of Romantic/Victorian criticism; Fancy; Primary and Secondary Imagination; Poetry vs Poem; Definition of Criticism; Role of Critic; Wordsworth’s opinion; Shelley’s ‘Defence of Poetry’; Arnold’s ‘Touchstone Method’; Arnold’s definition/role of critic; Walter Pater’s ‘Aestheticism’; Art for Art’s Sake.
                """
            },
            "Unit 4: New Criticism": {
                "texts": [
                    "W.K. Wimsatt and Monroe Beardsley – “The Intentional Fallacy”",
                    "Allen Tate – “Tension in Poetry”"
                ],
                "reference": """
                **Terms/Concepts:** Eliot’s Objective Correlative; Dissociation of Sensibility; Unification of Sensibility; Tradition and the Individual Talent; Tension, Extension, Intension; Heresy of Paraphrase; Intentional Fallacy; Affective Fallacy; Organic Form; Texture; I.A. Richards on Practical Criticism.
                """
            }
        },
        "Paper IV: Language: Basic Concepts (PAENG104)": {
            "Unit 1: Language and Linguistics": {
                "texts": [
                    "Scientific Study of Language vs Traditional Approaches",
                    "Scope & Branches (Sociolinguistics, Psycholinguistics, etc.)"
                ],
                "reference": """
                **Topics:** Linguistics as a Scientific Study of Language; Traditional Approaches vs Modern Linguistics; Scope of Linguistics; Branches: Sociolinguistics, Psycholinguistics, Comparative, Historical, Stylistics, Theoretical, Descriptive, Dialectology, Applied linguistics.
                """
            },
            "Unit 2: Levels of Structural Organization": {
                "texts": [
                    "Phonology: IPA, Cardinal Vowels, Suprasegmentals",
                    "Morphology: Morphemes, Word Formation",
                    "Semantics: Sense Relations, Lexical Semantics",
                    "Syntax: TG Grammar, IC Analysis, Deep vs Surface Structure"
                ],
                "reference": """
                **Phonology:** Nature/features/significance of phonetics; Organs of Speech; Classification of vowels/consonants; Cardinal Vowels; Phonetic transcription; Suprasegmental features (Intonation, Stress).
                **Morphology:** Definition/scope; Classification of Morphemes; Word formation processes.
                **Semantics:** Words as meaningful units (Reference/Sense, Sense Relations); Types of meaning; Lexical Semantics (Synonymy, Antonymy, Hyponymy, Homonymy); Sentence meaning.
                **Syntax:** Traditional vs Structural Descriptive vs Prescriptive; Grammaticality vs Acceptability; IC Analysis (constituent, immediate constituent, labelled bracketing); Limitations of IC analysis; Phrase Structure grammar (PS rules & limitations); TG Grammar Components (transformational/generative); Deep vs Surface Structure; Transformational rules (Negative, Interrogation, Tag Question, Passive, Adverbalization, Relativization, Coordination).
                """
            },
            "Unit 3: Introduction to English Language": {
                "texts": [
                    "History of English: Old, Middle, Early Modern, Late Modern",
                    "Foreign Influences: Greek, Latin, French, Scandinavian",
                    "Standard English & Received Pronunciation"
                ],
                "reference": """
                **Topics:** What is language? Characteristics; Varieties of Language; Origins of Language; Biological Basis (Language and Brain); Origin of English; History (Old, Middle, Early Modern, Late Modern); Foreign influence (Greek, Latin, French, Scandinavian, Indian Languages - Vocab, Grammar, Pronunciation); Standard English; Received Pronunciation.
                """
            },
            "Unit 4: Theories of Language": {
                "texts": [
                    "Classical Theories (Greek, Darwin, Indian School)",
                    "Formalist (Saussure, Chomsky)",
                    "Functionalist (Prague School, Firthian)"
                ],
                "reference": """
                **Classical:** Greek/Egyptian Theories; Darwin’s Theory of Evolution; Indian School (Patanjali, Bhartrihari, Panini).
                **Formalist:** Ferdinand Saussure; Roman Jakobson; Copenhagen School; Noam Chomsky (Universal Grammar, Nativism).
                **Functionalist:** Prague Linguistic School; Firthian Linguistics; Neo-Firthian Linguistics. (competence vs performance, model vs data-oriented, mentalistic vs sociological, theoretical vs applied).
                """
            }
        }
    },
    "Semester II": {
        "Paper V: Drama (PAENG201)": {
            "Unit 1: Elizabethan and Jacobean Period": {
                "texts": [
                    "William Shakespeare: The Merchant of Venice",
                    "Christopher Marlowe: Dr. Faustus"
                ],
                "reference": """
                **Socio-cultural/Political:** Feudalism and Social Status; Ecclesiastical/Church Control; Printing and Literacy; Travel and Exploration under Tudor reign and Early Stuarts.
                **Forms/Genres/Movements:** Miracle plays, Moralities, Interludes, Renaissance, Humanism, Reformation, Elizabethan Stage, University Wits, Shakespearean Plays, Blank Verse, Comedy of Humours.
                **Representative Dramatists:** Thomas Kyd, Christopher Marlowe, John Lily, Ben Jonson, Thomas Dekker, John Heywood, George Chapman, Cyril Tourneur, John Webster, Beaumont, John Fletcher, Philip Massinger, Thomas Middleton, William Rowley, John Ford, James Shirley, William Shakespeare, Robert Greene, Thomas Lodge.
                """
            },
            "Unit 2: The Restoration Period": {
                "texts": [
                    "William Congreve: Way of the World",
                    "William Wycherley: The Country Wife"
                ],
                "reference": """
                **Socio-cultural/Political:** English Civil War, Puritan Regime, Restoration, Rise of Party Politics, Age of Satire.
                **Forms/Genres/Movements:** Neo-Classicism, Heroic plays, Musical Comedy, Comedy of Manners, Restoration Comedy.
                **Representative Dramatists:** John Dryden, Sir John Etherege, Sir Charles Sedley, William Wycherley, William Congreve, George Farquhar, Sir John Vanbrugh, John Gay, Roger Boyle, Joanna Baillie.
                """
            },
            "Unit 3: Drama of 18th & 19th Century": {
                "texts": [
                    "Oliver Goldsmith: She Stoops to Conquer",
                    "G. B. Shaw: Candida"
                ],
                "reference": """
                **Socio-cultural/Political:** Impact of Industrial Revolution; French Revolution; Victorian age literary characteristics; Darwinism; Age of Science; Age of Faith and Doubt (Victorian Dilemma); Victorian compromise/conservatism; Victorian concept of morality; Age of Reason.
                **Forms/Genres/Movements:** Aesthetic Movement, Pre-Raphaelite Movement, Medievalism.
                **Representative Dramatists:** Colley Cibber, Richard Steele, George Lillo, Ambrose Philips, Henry Fielding, Oliver Goldsmith, Hugh Kelley, Richard Cumberland, R. B. Sheridan, T. W. Robertson, Sir Arthur Wing Pinero, Henry Arthur Jones, G. B. Shaw, S. M. Synge.
                """
            },
            "Unit 4: Modernism and After": {
                "texts": [
                    "Shelagh Delaney: A Taste of Honey",
                    "T. S. Eliot: Murder in the Cathedral"
                ],
                "reference": """
                **Socio-cultural/Political:** World War I and II and Interwar Period; Marxist Ideology and influence of Russian Experiment; Post-World War I and II developments.
                **Trends and Movements:** Existentialism, Absurd Drama, Poetic Drama, Realism, The Movement, features of Modernism, Postmodernism.
                **Representative Dramatists:** T. S. Eliot, Terence Rattigan, Samuel Beckett, John Osborne, Harold Pinter, Arnold Wesker, John Arden, John Whiting, Brendan Behan, Shelagh Delaney, Robert Bolt.
                """
            }
        },
        "Paper VI: Fiction (PAENG202)": {
            "Unit 1: Defoe to Romantic Fiction": {
                "texts": [
                    "Daniel Defoe: Robinson Crusoe",
                    "Mary Shelley: Frankenstein"
                ],
                "reference": """
                **Socio-cultural/Political:** Union of Parliament (1707); Battle of Culloden; New British identity; Anti-Scottish sentiment; Multinational voices.
                **Forms/Literary Trends:** Gothic Novel; early Science Fiction; Romances; Fiction; Sentimental novel (novel of sensibility); Novels of manners; Essays; Prose.
                **Representative Fiction Writers:** Daniel Defoe, Afra Behn, Samuel Richardson, Mary Wollstonecraft Shelley, Henry Fielding.
                """
            },
            "Unit 2: Nineteenth Century Fiction": {
                "texts": [
                    "Emily Bronte: Wuthering Heights",
                    "Thomas Hardy: Tess of the d’Urbervilles"
                ],
                "reference": """
                **Socio-cultural/Political:** Restoration impact; Rise of Prose and Fiction; Rise of Social Novel; Industrialization; Reform Act of 1832; Politics; Novel of Satire; Darwinism; Age of Science; Age of Faith and Doubt (Victorian Dilemma); Victorian compromise/conservatism; Victorian concept of morality.
                **Forms/Genres/Movements:** Age of political satire; Literary Realism; Supernatural and fantastic fiction.
                **Representative Novelists:** Bronte Sisters, George Eliot, Jane Austen, Thomas Hardy, Elizabeth Gaskell, Samuel Butler, John Galsworthy.
                """
            },
            "Unit 3: Twentieth Century Fiction": {
                "texts": [
                    "William Golding: Lord of the Flies",
                    "Michael Ondaatje: The English Patient"
                ],
                "reference": """
                **Socio-cultural/Political:** Age of Ideologies; Influence of Science, Technology and Psychology; World War I & II and Interwar Period; Marxist Ideology/Russian Experiment; Post-World War II developments; Cold War.
                **Forms/Genres/Movements:** Modernism; Science Fiction; Meta-fiction; Magic Realism; Interior Monologue; Oedipus Complex; Psychological Novel; Stream of Consciousness; Graphic Fiction.
                **Representative Novelists:** James Joyce, Virginia Woolf, William Golding, D.H. Lawrence, Joseph Conrad, E. M. Forster, H.G. Wells.
                """
            },
            "Unit 4: Twenty First Century": {
                "texts": [
                    "David Mitchell: Cloud Atlas",
                    "Sarah Waters: Little Stranger"
                ],
                "reference": """
                **Socio-cultural/Political:** Globalization and literature; Age of social media; Adaptations of traditional movements.
                **Trends and Movements:** Digital Literatures; Revolution in communication technology; Short fiction.
                **Representative Novelists:** Michael Chabon, Jennifer Egan, Ben Fountain, Ian McEwan, Chimamanda Ngozi Adichie, Zadie Smith, Jeffrey Eugenides.
                """
            }
        },
        "Paper VII: Literary Theory (PAENG203)": {
            "Unit 1: Structuralism, Post-Structuralism": {
                "texts": [
                    "Roland Barthes – “The Death of the Author”",
                    "Jacques Derrida – “Structure, Sign and Play...”",
                    "Jean Baudrillard – “Simulacra and Simulations”"
                ],
                "reference": """
                **Terms/Concepts:** Text and writing (Ecriture); Sign (Signifier/Signified); Langue and Parole; Transcendental signified; Aporia; Difference; Discourse.
                """
            },
            "Unit 2: Gender, Subaltern, Psychoanalysis": {
                "texts": [
                    "Judith Butler – “Subjects of Sex/Gender/Desire”",
                    "Gayatri Spivak – “Can the Subaltern Speak?”",
                    "Juliet Mitchell – “Femininity, Narrative and Psychoanalysis”"
                ],
                "reference": """
                **Terms/Concepts:** Gender; Masculinity; Femininity; Phallogocentric discourse; Gynocriticism; Subaltern; Hybridity; Id, Ego, Superego; Oedipus Complex; Sublimation; Symbolism.
                """
            },
            "Unit 3: Reader Response, Marxism, New Historicism": {
                "texts": [
                    "Stanley Fish - “Interpreting the Variorum”",
                    "Fredric Jameson- “The Politics of Theory”",
                    "Stephen Greenblatt – “Resonance and Wonder”"
                ],
                "reference": """
                **Terms/Concepts:** Phenomenology; Implied Reader; Affective Stylistics; Interpretative Communities; Base and Superstructure; Ideology; Hegemony; Political Unconscious; Circulation; Context; Culture; History and Narrative.
                """
            },
            "Unit 4: Postcolonialism, Ecocriticism, Technocriticism": {
                "texts": [
                    "Ashcroft, Griffith, Tiffins - “Cutting the Ground”",
                    "Cheryll Glotfelty - “Literary Studies in an age of Environmental Crisis”",
                    "Donna Haraway - “A Cyborg Manifesto”"
                ],
                "reference": """
                **Terms/Concepts:** Colonialism; Orientalism; Hybridity; Subaltern; Anthropocentrism and Ecocentrism; Pastoralism; Ecofeminism; Scientific Progress; Technoethics; Afrofuturism; Science Fiction (Space Opera, Cyberpunk, Biopunk).
                """
            }
        },
        "Paper VIII: English in Use (PAENG204)": {
            "Unit 1: Pragmatics": {
                "texts": [
                    "Speech Act Theory, Cooperative Principles, Politeness Principles",
                    "Implicature, Presupposition, Reference"
                ],
                "reference": """
                **Topics:** Introduction; Pragmatics and Nature of Language; Difference between Semantics and Pragmatics; Implicature; Presupposition; Speech Act Theory; Cooperative Principles; Politeness Principles; Reference.
                """
            },
            "Unit 2: Sociolinguistics": {
                "texts": [
                    "Regional and Social Dialects, Pidgins and Creoles",
                    "Speech Communities, Register, Style, Genre"
                ],
                "reference": """
                **Topics:** Regional and Social Dialects; Pidgins and Creoles; Codes; Speech Communities; Genre; Registers: Types, Features and Markers; Style: On the scale of formality.
                """
            },
            "Unit 3: Varieties of English": {
                "texts": [
                    "Standard vs Non-Standard English",
                    "Native vs Non-Native Varieties, World Englishes",
                    "Process of Standardization"
                ],
                "reference": """
                **Topics:** Dialects of English; Standard English and Non Standard English; Native and Non-Native Varieties of English; Process of Standardization; English-Based Pidgins and Creoles; Notion of international/global/world English.
                """
            },
            "Unit 4: English in India": {
                "texts": [
                    "History of English in India",
                    "Indianization of English, Features of Indian English",
                    "English in Indian Literature and Media"
                ],
                "reference": """
                **Topics:** History of English in India (Rise and Growth Pre-Independence); Status and development Post-Colonial Period; English Language Politics in India; Role of English in Indian Multilingualism; Current Status; English in Indian Literature and Media; Indianisation of English; Features and Structures of English in India.
                """
            }
        }
    }
}



def get_zhipu_client():
    api_key = os.getenv("ZHIPU_API_KEY")
    if not api_key:
        try:
            api_key = st.secrets.get("ZHIPU_API_KEY")
        except:
            pass
    if not api_key:
        st.error("⚠️ API Key not found.")
        return None
    return ZhipuAI(api_key=api_key)

def generate_exam_content(unit_name, pasted_text, additional_points, syllabus_reference, client):
    prompt = f"""
    You are a strict Professor of English at the University of Mumbai preparing students for their M.A. exams.
    
    **TASK:** 
    Analyze the provided text and generate potential 15-mark exam questions based on the University of Mumbai syllabus context provided.
    
    **SELECTED UNIT:** {unit_name}
    
    **SYLLABUS CONTEXT (What is extremely important for the exam):**
    {syllabus_reference}
    
    **ADDITIONAL POINTS (User Focus):**
    {additional_points}
    
    **PASTED TEXT CONTENT:**
    {pasted_text}
    
    **INSTRUCTIONS:**
    1. Identify the most critical themes in the text that align with the Syllabus Context.
    2. Generate **2-3 variations** of 15-mark exam questions that would appear for this unit.
    3. Provide a detailed, high-quality answer for **EACH** question listed. (Do not only answer the first one).
    4. **Word Count:** Each answer must be substantial, aiming for a minimum of 800 words.
    5. **Formatting:** 
       - Do NOT include a "References" or "Further Reading" section at the end.
       - Use **double asterisks** (e.g., **this is important**) to mark points that are absolutely essential for scoring full marks. Do NOT use HTML span tags. Use Markdown bold syntax.
    
    **OUTPUT FORMAT:**
    **Question 1:** [Text]
    **Answer 1:** [Detailed 800+ word answer with Markdown bold highlights]
    
    **Question 2:** [Text]
    **Answer 2:** [Detailed 800+ word answer with Markdown bold highlights]
    """

    try:
        response = client.chat.completions.create(
            model="GLM-4.7-Flash", 
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=False,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating content: {str(e)}"

def main():
    st.title("M.A. English Exam Generator (MU)")
    st.caption("Likely Questions Generator. (Please do not over-rely on this.)")

    with st.sidebar:
        st.header("1. Select Unit")
        semester = st.selectbox("Semester", list(SYLLABUS_DATA.keys()))
        papers = list(SYLLABUS_DATA[semester].keys())
        selected_paper = st.selectbox("Paper", papers)
        
        units = list(SYLLABUS_DATA[semester][selected_paper].keys())
        selected_unit = st.selectbox("Unit", units)
        
        unit_data = SYLLABUS_DATA[semester][selected_paper][selected_unit]
        full_reference = unit_data.get("reference", "No reference data available.")
        prescribed_texts = unit_data.get("texts", [])

    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("2. Paste Text Content")
        st.write("Copy and paste the text of the specific chapter/poem/essay you are studying below.")
        
        text_content = st.text_area(
            "Paste Chapter Text Here...", 
            height=400, 
            placeholder="Paste the text content here...",
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.subheader("3. Generate Exam Prep")
        if st.button("✨ Generate 15-Mark Q&A", type="primary", disabled=not text_content):
            client = get_zhipu_client()
            if client:
                with st.spinner("Analyzing text against syllabus... (This may take a moment)"):
                   
                    add_points = st.session_state.get('additional_points', "")
                    result = generate_exam_content(selected_unit, text_content, add_points, full_reference, client)
                    st.session_state['generated_result'] = result
            else:
                st.error("API Key Missing")

    with col_right:
        st.subheader("Syllabus Reference")
        st.info("📚 **Extremely Important Exam Context (Section A):**")
        st.markdown(full_reference)
        
        st.markdown("---")
        st.markdown("### Prescribed Texts (Section B):")
        for t in prescribed_texts:
            st.markdown(f"- {t}")
            
        st.markdown("---")
        st.markdown("### Additional Important Points")
        st.write("Add any specific points, themes, or professor notes you want the AI to focus on:")
        add_points_input = st.text_area("Type additional focus points here...", height=150, key="additional_points_input")
        st.session_state['additional_points'] = add_points_input

    if 'generated_result' in st.session_state:
        st.markdown("---")
        st.subheader("Generated Exam Material")
        
      
        st.markdown(st.session_state['generated_result'])

if __name__ == "__main__":
    main()