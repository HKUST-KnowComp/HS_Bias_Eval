"""
Constants shared across files.
"""
import re
en_vector_file_path = '../data/bi-embedding-babylon78/wiki.en.vec'
ar_vector_file_path = '../data/bi-embedding-babylon78/wiki.ar.vec'
fr_vector_file_path = '../data/bi-embedding-babylon78/wiki.fr.vec'
#ENGLISH
keywords_english = ['islam', 'terrorism', 'asian', 'arab', 'fuck', 'twat', 'muslim', 'christian', 'jew', 'pig', 'bitch', 'feminazi', 'woman', 'women', 'faggot', 'retard']
keywords_general_english = ['islam', 'terrorism', 'asian', 'arab', 'fuck', 'twat', 'muslim', 'christian', 'jew', 'pig', 'bitch', 'feminazi', 'woman', 'women', 'faggot', 'retard']
keywords_origin_english = ['immigrant', 'nigger', 'nigga', 'asian', 'dirty', 'pig', 'ching', 'chong', 'negro', 'mexican', 'spic', 'shithole', 'redneck', 'alien', 'country', 'countries', 'chinaman', 'raghead', 'camel', 'chinaman', 'wetback']
keywords_religion_english = ['muzzie', 'muslim', 'terrorist', 'attack', 'christian', 'jew', 'pig', 'terrorism', 'invasion', 'jihadi', 'raghead', 'camel']
keywords_gender_english =  ['bitch', 'feminazi', 'woman', 'women', 'cunt', 'dyke', 'twat', 'faggot', 'trans']
keywords_disability_english = ['mongol', 'mongoloid', 'mongy', 'downy', 'retard']
keywords_other_english = ['conspiracy', 'theorist', 'leftist', 'theory']
waseem_hovy_keywords = ['mkr', 'asian', 'drive', 'feminazi', 'immigrant', 'nigger', 'sjw', 'womenagainstfeminism', 'blameonenotall', 'islam', 'terrorism', 'notallmen','victimcard', 'victim', 'card', 'arab', 'terror', 'gamergate', 'jsil', 'racecard', 'race']
waseem_hovy_origin_keywords =['asian', 'immigrant', 'nigger', 'arab', 'race', 'racecard'] 
waseem_hovy_religion_keywords =['islam', 'terrorism', 'arab'] 
waseem_hoy_gender_keywords = ['mkr', 'feminazi', 'women', 'victim','womenagainstfeminism', 'sjw', 'blamenonenotall', 'notallmen', 'victimcard', 'gamergate']
#keywords_target_english = [keywords_origin_en, keywords_religion_en, keywords_gender_en, keywords_disability_en, keywords_other_en]
#keywords_target_dict_english = {'origin': keywords_origin_en, 'religion': keywords_religion_en, 'gender': keywords_gender_en, 'disability': keywords_disability_en, 'other': keywords_other_en}

#PORTUGUESE
keywords_portuguese = ['discurso', 'odio', 'fufas', 'sapatao','lugardemulherenacozinha' ] #changed 'discurso de odio' to 'discurso' 'odio'

#ITALIAN
keywords_italian = ['invadere', 'invasione', 'basta', 'fuori', 'comunist', 'african', 'barcon']

#GERMAN
keywords_german = ['pack', 'aslyanten', 'wehrdich', 'krimmigranten','rapefugees', 'islamfaschisten', 'refugeesnotwelcome', 'islamisierung', 'asylanteninvasion', 'scharia'] #changed the hashtags into words

#fRENCH
keywords_french = ['invasion', 'refugie', 'renoi', 'noir', 'arabe', 'rebeu', 'migrant', 'negro', 'sale', 'juif', 'terrorisme', 'islam', 'mongol', 'attarde', 'feministe', 'sale', 'gauchiste']
keywords_origin_french = ['invasion', 'refugie', 'refugies', 'renois', 'renoi', 'noir', 'arabe', 'rebeu', 'arabes', 'rebeus', 'migrant', 'migrants', 'africain', 'negre', 'negro', 'afrique', 'sale'] 
keywords_religion_french = ['islam', 'musulman', 'invasion', 'terroriste', 'islamisation', 'juif', 'chretien', 'sale']
keywords_disability_french = ['attarde', 'mongol', 'debile' ]
keywords_gender_french = ['feministe', 'pute', 'pede']
keywords_other_french = ['gauchiste', 'complotiste']
keywords_general_french = ['sale']
#keywords_target_french = [keywords_origin_fr, keywords_religion_fr, keywords_gender_fr, keywords_disability_fr, keywords_other_fr]
#keywords_target_dict_french = {'origin': keywords_origin_fr, 'religion': keywords_religion_fr, 'gender': keywords_gender_fr, 'disability': keywords_disability_fr, 'other': keywords_other_fr}

#ARABIC
keywords_arabic=[ 'إلحاد', 'دروز','كلب','بايرة', 'حريم', 'مراة', 'وسخ','بنات','بعير', 'علماني', 'شيعة', 'سنّة', 'يهود', 'مسيح', 'هندوس','إسلام', 'علمانية']
keywords_origin_arabic = ['لاجئ', 'اكراد', 'سوري', 'ايران', 'سعودية', 'كردي', 'بول', 'البعير','افارقة', 'بعير']
keywords_religion_arabic = ['شيعي', 'رافضي', 'علوي', 'علماني', 'شيعة', 'سنة', 'يهود', 'مسيح', 'هندوس', 'إلحاد', 'دروز']
keywords_arabic_general_correct_spelling = ['بايرة', 'حريم', 'مرأة', 'متبرجة', 'وسخ','بنات','بعير','رافضة', 'إسلام', 'علمانية', 'شيعة', 'سنّة', 'يهود', 'مسيح', 'هندوس', 'إلحاد', 'دروز', 'كرد','افارقة','سوري', 'إيران', 'سعودية', 'بول']
keywords_gender_arabic = ['بايرة', 'حريم', 'مراة', 'متبرجة', 'ديوث', 'فمينيست', 'بنات', 'بنت', 'نساء', 'منحرفة']
keywords_other_arabic = ['وسخ']
#keywords_target_arabic = [keywords_origin_ar, keywords_religion_ar, keywords_gender_ar, keywords_other_ar]
#keywords_target_dict_arabic = {'origin': keywords_origin_ar, 'religion': keywords_religion_ar, 'gender': keywords_gender_ar,'other': keywords_other_ar}

#INSONESIAN
list_keywords_indonesian = ['alay', 'ampas', 'buta', 'keparat', 'anjing', 'anjir', 'babi', 'bacot', 'bajingan', 'banci', 'bandot', 'buaya', 'bangkai', 'bangsat', 'bego', 'bejat', 'bencong', 'berak', 'bisu', 'celeng', 'jancuk', 'bodoh', 'berengsek', 'budek', 'burik', 'jamban', 'cocot', 'congor', 'culun', 'cupu', 'dongok', 'dungu', 'edan', 'tai', 'ngewe', 'geblek', 'gembel', 'gila', 'goblok', 'iblis', 'idiot', 'jablay', 'jembud', 'jembut', 'jijik', 'kacrut', 'kafir', 'modar', 'kampang', 'kampret', 'kampungan', 'kimak', 'kontol', 'kunti', 'tuyul', 'kunyuk', 'mampus', 'memek', 'monyet', 'najis', 'nete', 'ngentot', 'noob', 'pecun', 'perek', 'sampah', 'sarap', 'setan', 'silit', 'bokong', 'sinting', 'sompret', 'sontoloyo', 'terkutuk', 'titit', 'pantat', 'tolol', 'udik', 'antek', 'asing', 'ateis', 'sitip', 'autis', 'picek', 'ayam kampus', 'bani kotak', 'bispak', 'bisyar', 'bokep', 'bong', 'cacat', 'cct', 'cebong', 'taplak', 'cungkring', 'gay', 'gembrot', 'gendut', 'hina', 'homo', 'komunis', 'koreng', 'krempeng', 'lengser', 'lesbi', 'lgbt', 'lonte', 'mucikari', 'munafik', 'ngaceng', 'nista', 'kejam', 'onta', 'panastak', 'panasbung', 'bani', 'pasukan nasi', 'porno', 'seks', 'rejim', 'rezim', 'sange', 'serbet', 'sipit', 'transgender']
BIAS_METRICS = ['b1', 'b2', None]
SIMILARITY_MEASURES = ['fasttext', 'hate_speech', 'wordnet', None]
#dictionary that maps lanuage names to laanguage codes, you can introduce other languages an download their embeddings
LANGUAGE_CODE = {'arabic': 'ar', 'english': 'en', 'french': 'fr', 'italian': 'it', 'portuguese': 'pt', 'indonesian': 'id', 'german': 'de'}
LANGUAGES = ['arabic', 'english', 'french', 'italian', 'idonesian', 'portuguese', 'german']
KEYWORDS_LANGUAGE = {'arabic':keywords_arabic, 'english':keywords_english, 'french':keywords_french, 'italian':keywords_italian, 'idonesian':list_keywords_indonesian, 'portuguese':keywords_portuguese, 'german':keywords_german}

