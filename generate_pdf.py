import os
import pdfkit

template_file = 'ResultsTemplate.htm'

def convert_html_to_pdf(html_content, pdf_path):
    try:
        pdfkit.from_string(html_content, pdf_path)
        print(f'PDF generated and saved at {pdf_path}')
    except Exception as e:
        print(f'PDF generation failed: {e}')

def generate_pdf(disorder, patterns, count):
    new_lines = []

    genetic_markers = []
    risk_factors = []
    recommendations = []

    for i in disorder:
        if i == "no diseases found in the provided DNA sequence.":
            genetic_markers.append("N/A")
            risk_factors.append("N/A")
            recommendations.append("N/A")

            break

        elif i == "lactose intolerance":
            genetic_markers.append("The C/T-13910 SNP in the MCM6 gene is associated with lactase persistence, allowing continued lactase production into adulthood. The C/T-13910 SNP in the MCM6 gene, with the T allele, is linked to lactase non-persistence, resulting in reduced lactase production after childhood.")
            risk_factors.append("Genetic factors, such as the C/T-13910 SNP in the MCM6 gene, play a role in determining an individual's susceptibility to lactose intolerance. Lactose intolerance is more commonly observed in certain ethnic groups, including people of African, Asian, Native American, and Hispanic descent. Aging is a significant risk factor, as the production of lactase tends to decrease naturally after childhood, making adults more prone to lactose intolerance. Gastrointestinal disorders like celiac disease, Crohn's disease, and irritable bowel syndrome can elevate the risk of developing lactose intolerance. Infections or injuries to the digestive system may lead to a temporary reduction in lactase production, contributing to lactose intolerance. Certain medical treatments, such as chemotherapy or radiation therapy, can impact the digestive system and increase the risk of lactose intolerance. Some medications, especially those affecting the gastrointestinal system, may interfere with lactose digestion and absorption, contributing to intolerance. Premature infants may have lower levels of lactase, increasing their susceptibility to lactose intolerance. A diet low in dairy products during childhood may contribute to decreased lactase production, potentially leading to lactose intolerance later in life. Changes in the composition of gut microbiota can influence lactose digestion and contribute to the development of lactose intolerance.")
            recommendations.append("Gradually introduce small amounts of dairy into your diet to gauge tolerance levels, starting with lactose-free or low-lactose options. Take lactase supplements before consuming dairy products to aid in the digestion of lactose and minimize discomfort. Opt for lactose-free or reduced-lactose versions of milk and dairy products, widely available in most grocery stores. Experiment with different dairy sources, such as hard cheeses or yoghurt, to identify options that are better tolerated. Monitor portion sizes when consuming dairy, as smaller amounts may be better tolerated, allowing you to enjoy dairy without discomfort. Pair dairy with other foods as part of a meal rather than consuming it on an empty stomach to improve digestion. Ensure an adequate intake of calcium by exploring non-dairy sources like leafy green vegetables, fortified plant-based milk, and calcium supplements if necessary. Consult with a registered dietitian for personalized advice on managing lactose intolerance and planning a well-balanced diet that meets your nutritional needs. Read food labels carefully to identify hidden sources of lactose in processed and packaged foods, helping you avoid unintentional consumption. Maintain a food diary to track dairy consumption and associated symptoms, aiding in the identification of specific triggers and informing dietary adjustments. Stay hydrated, especially if diarrhea is a symptom of lactose intolerance, as adequate water intake can help manage symptoms and prevent dehydration. Consider incorporating probiotics into your diet, as some individuals find relief from lactose intolerance symptoms with their use. Consult with a healthcare professional before starting any supplementation.")

        elif i == "haemophilia":
            genetic_markers.append("Haemophilia A, characterized by Factor VIII deficiency, is associated with genetic mutations in the F8 gene. Haemophilia B, characterized by Factor IX deficiency, is linked to genetic mutations in the F9 gene.")
            risk_factors.append("Advancing age is a common risk factor for cardiovascular diseases, as the likelihood of developing such conditions increases with age. Men generally face a higher risk of cardiovascular issues, while the risk for women tends to rise after menopause. A family history of heart disease or stroke can elevate an individual's risk of experiencing similar cardiovascular events. Certain genetic factors may predispose individuals to cardiovascular conditions, emphasizing the importance of understanding one's family medical history. Smoking introduces harmful chemicals that can damage blood vessels and heart tissues, significantly increasing the risk of cardiovascular diseases. High blood pressure, or hypertension, places strain on the heart and arteries, contributing to an increased risk of cardiovascular events. Elevated levels of LDL (bad) cholesterol and low levels of HDL (good) cholesterol are associated with an increased risk of atherosclerosis and cardiovascular diseases. Individuals with diabetes face a higher risk of developing cardiovascular diseases, emphasizing the importance of managing blood sugar levels. Excess body weight, particularly around the abdomen, is a risk factor for heart disease, highlighting the importance of maintaining a healthy weight. Lack of regular physical activity is associated with an increased risk of heart disease, underscoring the importance of an active lifestyle. Diets high in saturated fats, trans fats, sodium, and low in fruits and vegetables contribute to heart disease risk, emphasizing the role of a healthy diet. Excessive alcohol consumption can raise blood pressure and contribute to heart disease, highlighting the importance of moderate drinking. Chronic stress may contribute to unhealthy behaviors that increase the risk of heart disease, emphasizing the importance of stress management. Untreated sleep apnea, a condition characterized by interrupted breathing during sleep, can contribute to hypertension and heart problems, emphasizing the importance of addressing sleep-related issues. Individuals with a history of previous cardiovascular events, such as heart attacks or strokes, are at an increased risk of experiencing future events, underscoring the importance of ongoing monitoring and preventive measures.")
            recommendations.append("Schedule regular health check-ups to monitor blood pressure, cholesterol levels, and overall cardiovascular health with healthcare professionals. Adopt a heart-healthy diet rich in fruits, vegetables, whole grains, and lean proteins, while minimizing saturated fats, trans fats, cholesterol, and sodium. Engage in regular physical activity, aiming for at least 150 minutes of moderate-intensity exercise or 75 minutes of vigorous-intensity exercise per week. Achieve and maintain a healthy weight through a balanced diet and regular physical activity. If you smoke, quit smoking, and seek support from healthcare professionals or smoking cessation programs. Consume alcohol in moderation, if at all, with guidelines suggesting up to one drink per day for women and up to two drinks per day for men. Practice stress-management techniques such as deep breathing, meditation, yoga, or other relaxation methods to promote overall well-being. Ensure sufficient, quality sleep each night and address sleep disorders, such as sleep apnea, if present. Manage diabetes through regular monitoring of blood sugar levels, medication adherence, and lifestyle modifications. Adhere to prescribed medication for conditions like hypertension or high cholesterol, attending regular follow-up appointments with healthcare providers. Understand your family medical history and share it with healthcare providers for a comprehensive cardiovascular risk assessment. Stay informed about the latest developments in cardiovascular health and follow guidelines for heart-healthy living. Seek support from friends, family, or community groups to maintain motivation for healthy lifestyle changes. Consider counselling or therapy if dealing with chronic stress, anxiety, or depression that may impact heart health. Learn and recognize the signs of a heart attack or stroke, and know the appropriate emergency response measures for prompt action.")

        else:  
            genetic_markers.append("Deletions, mutations, or duplications in the SHANK3 gene are associated with certain cases of autism spectrum disorder (ASD), impacting synaptic function crucial for neural communication. Variations, deletions, or mutations in the CNTNAP2 gene have been identified in individuals with ASD, particularly affecting neural circuit formation related to language development and social communication. Variations or mutations in the MET gene, involved in brain development, have been linked to an increased risk of ASD, especially in cases with co-occurring gastrointestinal issues. Mutations or variations in NLGN and NRXN genes, which play roles in synapse formation, are associated with disruptions in neural connectivity and have been implicated in ASD. Variations or mutations in the FOXP2 gene, associated with language development, contribute to language difficulties observed in some individuals with ASD.")
            risk_factors.append("A family history of autism spectrum disorder (ASD) or other developmental disorders increases the likelihood of ASD in subsequent generations due to certain genetic factors. Older parental age, particularly in fathers, has been associated with a slightly higher risk of ASD in their offspring. Babies born prematurely or with low birth weight may have an elevated risk of developing ASD. Prenatal and perinatal complications, such as exposure to certain medications, maternal illness, or birth complications, are potential risk factors for ASD. Prenatal exposure to certain drugs, medications, or environmental toxins may contribute to an increased risk of ASD. Maternal health conditions like diabetes, obesity, and certain infections during pregnancy may be associated with a higher risk of ASD. Certain infections or illnesses during early childhood have been suggested to be linked to an increased risk of ASD, although the evidence is not conclusive. Boys are diagnosed with ASD more frequently than girls, contributing to the understanding that being male is a potential risk factor for ASD. Some studies suggest a potential link between lower socioeconomic status and an increased risk of ASD, though the relationship is complex and influenced by various factors. Maternal and paternal mental health conditions, such as depression or anxiety, may be associated with a slightly increased risk of ASD in their children.")
            recommendations.append("Seek early intervention services such as speech therapy and occupational therapy to address developmental challenges in individuals with autism spectrum disorder (ASD). Collaborate with educators to create and implement an Individualized Education Plan (IEP) tailored to the unique needs and strengths of the individual with ASD. Provide a structured and predictable environment at home and in educational settings to enhance the comfort and security of individuals with ASD. Engage in social skills training programs to help individuals with ASD develop effective communication and interaction skills. Utilize visual aids, augmentative and alternative communication (AAC) devices, and other supports to facilitate communication for individuals with ASD. Implement sensory integration techniques to address sensory sensitivities or challenges commonly experienced by individuals with ASD. Consider behavioural therapy, such as Applied Behavior Analysis (ABA), to address challenging behaviours and reinforce positive ones. Attend training sessions and workshops to empower parents and caregivers with effective strategies for supporting individuals with ASD. Connect with local and online autism support groups and organizations to access information, share experiences, and find community support. Develop a transition plan that addresses the evolving needs of individuals with ASD as they move from childhood to adolescence and adulthood. Foster and encourage the unique interests and strengths of individuals with ASD, recognizing their potential for excellence in specific areas. Gradually introduce and promote independence in daily living skills, adapting tasks to the individual's abilities and preferences. Establish and maintain a consistent daily routine to provide individuals with ASD with a sense of predictability and security. Access therapeutic supports such as psychological counselling or psychotherapy to address mental health and emotional well-being. Advocate for inclusion and acceptance in schools, workplaces, and community settings to promote understanding and support for individuals with ASD.")
                        
    new_lines.append(
    """
        <html xmlns:v='urn:schemas-microsoft-com:vml'
        xmlns:o='urn:schemas-microsoft-com:office:office'
        xmlns:w='urn:schemas-microsoft-com:office:word'
        xmlns:m='http://schemas.microsoft.com/office/2004/12/omml'
        xmlns='http://www.w3.org/TR/REC-html40'>

        <head>
        <meta http-equiv=Content-Type content='text/html; charset=windows-1252'>
        <meta name=ProgId content=Word.Document>
        <meta name=Generator content='Microsoft Word 15'>
        <meta name=Originator content='Microsoft Word 15'>
        <link rel=File-List href='ResultsTemplate_files/filelist.xml'>
        <link rel=Edit-Time-Data href='ResultsTemplate_files/editdata.mso'>
        <!--[if !mso]>
        <style>
        v\:* {behavior:url(#default#VML);}
        o\:* {behavior:url(#default#VML);}
        w\:* {behavior:url(#default#VML);}
        .shape {behavior:url(#default#VML);}
        </style>
        <![endif]--><!--[if gte mso 9]><xml>
        <o:DocumentProperties>
        <o:Author>Alex</o:Author>
        <o:Template>Normal</o:Template>
        <o:LastAuthor>Alex Steiner</o:LastAuthor>
        <o:Revision>2</o:Revision>
        <o:TotalTime>1</o:TotalTime>
        <o:LastPrinted>2023-12-21T14:06:00Z</o:LastPrinted>
        <o:Created>2023-12-21T16:34:00Z</o:Created>
        <o:LastSaved>2023-12-21T16:34:00Z</o:LastSaved>
        <o:Pages>1</o:Pages>
        <o:Words>10215</o:Words>
        <o:Characters>58231</o:Characters>
        <o:Lines>485</o:Lines>
        <o:Paragraphs>136</o:Paragraphs>
        <o:CharactersWithSpaces>68310</o:CharactersWithSpaces>
        <o:Version>16.00</o:Version>
        </o:DocumentProperties>
        <o:OfficeDocumentSettings>
        <o:AllowPNG/>
        </o:OfficeDocumentSettings>
        </xml><![endif]-->
        <link rel=themeData href='ResultsTemplate_files/themedata.thmx'>
        <link rel=colorSchemeMapping href='ResultsTemplate_files/colorschememapping.xml'>
        <!--[if gte mso 9]><xml>
        <w:WordDocument>
        <w:SpellingState>Clean</w:SpellingState>
        <w:GrammarState>Clean</w:GrammarState>
        <w:TrackMoves>false</w:TrackMoves>
        <w:TrackFormatting/>
        <w:HyphenationZone>14</w:HyphenationZone>
        <w:PunctuationKerning/>
        <w:ValidateAgainstSchemas/>
        <w:SaveIfXMLInvalid>false</w:SaveIfXMLInvalid>
        <w:IgnoreMixedContent>false</w:IgnoreMixedContent>
        <w:AlwaysShowPlaceholderText>false</w:AlwaysShowPlaceholderText>
        <w:DoNotPromoteQF/>
        <w:LidThemeOther>IT</w:LidThemeOther>
        <w:LidThemeAsian>X-NONE</w:LidThemeAsian>
        <w:LidThemeComplexScript>X-NONE</w:LidThemeComplexScript>
        <w:Compatibility>
        <w:BreakWrappedTables/>
        <w:SnapToGridInCell/>
        <w:WrapTextWithPunct/>
        <w:UseAsianBreakRules/>
        <w:DontGrowAutofit/>
        <w:SplitPgBreakAndParaMark/>
        <w:EnableOpenTypeKerning/>
        <w:DontFlipMirrorIndents/>
        <w:OverrideTableStyleHps/>
        </w:Compatibility>
        <m:mathPr>
        <m:mathFont m:val='Cambria Math'/>
        <m:brkBin m:val='before'/>
        <m:brkBinSub m:val='&#45;-'/>
        <m:smallFrac m:val='off'/>
        <m:dispDef/>
        <m:lMargin m:val='0'/>
        <m:rMargin m:val='0'/>
        <m:defJc m:val='centerGroup'/>
        <m:wrapIndent m:val='1440'/>
        <m:intLim m:val='subSup'/>
        <m:naryLim m:val='undOvr'/>
        </m:mathPr></w:WordDocument>
        </xml><![endif]--><!--[if gte mso 9]><xml>
        <w:LatentStyles DefLockedState='false' DefUnhideWhenUsed='false'
        DefSemiHidden='false' DefQFormat='false' DefPriority='99'
        LatentStyleCount='376'>
        <w:LsdException Locked='false' Priority='0' QFormat='true' Name='Normal'/>
        <w:LsdException Locked='false' Priority='9' QFormat='true' Name='heading 1'/>
        <w:LsdException Locked='false' Priority='9' SemiHidden='true'
        UnhideWhenUsed='true' QFormat='true' Name='heading 2'/>
        <w:LsdException Locked='false' Priority='9' SemiHidden='true'
        UnhideWhenUsed='true' QFormat='true' Name='heading 3'/>
        <w:LsdException Locked='false' Priority='9' SemiHidden='true'
        UnhideWhenUsed='true' QFormat='true' Name='heading 4'/>
        <w:LsdException Locked='false' Priority='9' SemiHidden='true'
        UnhideWhenUsed='true' QFormat='true' Name='heading 5'/>
        <w:LsdException Locked='false' Priority='9' SemiHidden='true'
        UnhideWhenUsed='true' QFormat='true' Name='heading 6'/>
        <w:LsdException Locked='false' Priority='9' SemiHidden='true'
        UnhideWhenUsed='true' QFormat='true' Name='heading 7'/>
        <w:LsdException Locked='false' Priority='9' SemiHidden='true'
        UnhideWhenUsed='true' QFormat='true' Name='heading 8'/>
        <w:LsdException Locked='false' Priority='9' SemiHidden='true'
        UnhideWhenUsed='true' QFormat='true' Name='heading 9'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='index 1'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='index 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='index 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='index 4'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='index 5'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='index 6'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='index 7'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='index 8'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='index 9'/>
        <w:LsdException Locked='false' Priority='39' SemiHidden='true'
        UnhideWhenUsed='true' Name='toc 1'/>
        <w:LsdException Locked='false' Priority='39' SemiHidden='true'
        UnhideWhenUsed='true' Name='toc 2'/>
        <w:LsdException Locked='false' Priority='39' SemiHidden='true'
        UnhideWhenUsed='true' Name='toc 3'/>
        <w:LsdException Locked='false' Priority='39' SemiHidden='true'
        UnhideWhenUsed='true' Name='toc 4'/>
        <w:LsdException Locked='false' Priority='39' SemiHidden='true'
        UnhideWhenUsed='true' Name='toc 5'/>
        <w:LsdException Locked='false' Priority='39' SemiHidden='true'
        UnhideWhenUsed='true' Name='toc 6'/>
        <w:LsdException Locked='false' Priority='39' SemiHidden='true'
        UnhideWhenUsed='true' Name='toc 7'/>
        <w:LsdException Locked='false' Priority='39' SemiHidden='true'
        UnhideWhenUsed='true' Name='toc 8'/>
        <w:LsdException Locked='false' Priority='39' SemiHidden='true'
        UnhideWhenUsed='true' Name='toc 9'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Normal Indent'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='footnote text'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='annotation text'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='header'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='footer'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='index heading'/>
        <w:LsdException Locked='false' Priority='35' SemiHidden='true'
        UnhideWhenUsed='true' QFormat='true' Name='caption'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='table of figures'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='envelope address'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='envelope return'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='footnote reference'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='annotation reference'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='line number'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='page number'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='endnote reference'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='endnote text'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='table of authorities'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='macro'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='toa heading'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Bullet'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Number'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List 4'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List 5'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Bullet 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Bullet 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Bullet 4'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Bullet 5'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Number 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Number 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Number 4'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Number 5'/>
        <w:LsdException Locked='false' Priority='10' QFormat='true' Name='Title'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Closing'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Signature'/>
        <w:LsdException Locked='false' Priority='1' SemiHidden='true'
        UnhideWhenUsed='true' Name='Default Paragraph Font'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Body Text'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Body Text Indent'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Continue'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Continue 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Continue 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Continue 4'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='List Continue 5'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Message Header'/>
        <w:LsdException Locked='false' Priority='11' QFormat='true' Name='Subtitle'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Salutation'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Date'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Body Text First Indent'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Body Text First Indent 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Note Heading'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Body Text 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Body Text 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Body Text Indent 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Body Text Indent 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Block Text'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Hyperlink'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='FollowedHyperlink'/>
        <w:LsdException Locked='false' Priority='22' QFormat='true' Name='Strong'/>
        <w:LsdException Locked='false' Priority='20' QFormat='true' Name='Emphasis'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Document Map'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Plain Text'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='E-mail Signature'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Top of Form'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Bottom of Form'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Normal (Web)'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Acronym'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Address'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Cite'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Code'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Definition'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Keyboard'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Preformatted'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Sample'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Typewriter'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='HTML Variable'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Normal Table'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='annotation subject'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='No List'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Outline List 1'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Outline List 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Outline List 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Simple 1'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Simple 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Simple 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Classic 1'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Classic 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Classic 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Classic 4'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Colorful 1'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Colorful 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Colorful 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Columns 1'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Columns 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Columns 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Columns 4'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Columns 5'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Grid 1'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Grid 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Grid 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Grid 4'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Grid 5'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Grid 6'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Grid 7'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Grid 8'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table List 1'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table List 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table List 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table List 4'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table List 5'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table List 6'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table List 7'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table List 8'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table 3D effects 1'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table 3D effects 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table 3D effects 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Contemporary'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Elegant'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Professional'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Subtle 1'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Subtle 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Web 1'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Web 2'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Web 3'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Balloon Text'/>
        <w:LsdException Locked='false' Priority='39' Name='Table Grid'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Table Theme'/>
        <w:LsdException Locked='false' SemiHidden='true' Name='Placeholder Text'/>
        <w:LsdException Locked='false' Priority='1' QFormat='true' Name='No Spacing'/>
        <w:LsdException Locked='false' Priority='60' Name='Light Shading'/>
        <w:LsdException Locked='false' Priority='61' Name='Light List'/>
        <w:LsdException Locked='false' Priority='62' Name='Light Grid'/>
        <w:LsdException Locked='false' Priority='63' Name='Medium Shading 1'/>
        <w:LsdException Locked='false' Priority='64' Name='Medium Shading 2'/>
        <w:LsdException Locked='false' Priority='65' Name='Medium List 1'/>
        <w:LsdException Locked='false' Priority='66' Name='Medium List 2'/>
        <w:LsdException Locked='false' Priority='67' Name='Medium Grid 1'/>
        <w:LsdException Locked='false' Priority='68' Name='Medium Grid 2'/>
        <w:LsdException Locked='false' Priority='69' Name='Medium Grid 3'/>
        <w:LsdException Locked='false' Priority='70' Name='Dark List'/>
        <w:LsdException Locked='false' Priority='71' Name='Colorful Shading'/>
        <w:LsdException Locked='false' Priority='72' Name='Colorful List'/>
        <w:LsdException Locked='false' Priority='73' Name='Colorful Grid'/>
        <w:LsdException Locked='false' Priority='60' Name='Light Shading Accent 1'/>
        <w:LsdException Locked='false' Priority='61' Name='Light List Accent 1'/>
        <w:LsdException Locked='false' Priority='62' Name='Light Grid Accent 1'/>
        <w:LsdException Locked='false' Priority='63' Name='Medium Shading 1 Accent 1'/>
        <w:LsdException Locked='false' Priority='64' Name='Medium Shading 2 Accent 1'/>
        <w:LsdException Locked='false' Priority='65' Name='Medium List 1 Accent 1'/>
        <w:LsdException Locked='false' SemiHidden='true' Name='Revision'/>
        <w:LsdException Locked='false' Priority='34' QFormat='true'
        Name='List Paragraph'/>
        <w:LsdException Locked='false' Priority='29' QFormat='true' Name='Quote'/>
        <w:LsdException Locked='false' Priority='30' QFormat='true'
        Name='Intense Quote'/>
        <w:LsdException Locked='false' Priority='66' Name='Medium List 2 Accent 1'/>
        <w:LsdException Locked='false' Priority='67' Name='Medium Grid 1 Accent 1'/>
        <w:LsdException Locked='false' Priority='68' Name='Medium Grid 2 Accent 1'/>
        <w:LsdException Locked='false' Priority='69' Name='Medium Grid 3 Accent 1'/>
        <w:LsdException Locked='false' Priority='70' Name='Dark List Accent 1'/>
        <w:LsdException Locked='false' Priority='71' Name='Colorful Shading Accent 1'/>
        <w:LsdException Locked='false' Priority='72' Name='Colorful List Accent 1'/>
        <w:LsdException Locked='false' Priority='73' Name='Colorful Grid Accent 1'/>
        <w:LsdException Locked='false' Priority='60' Name='Light Shading Accent 2'/>
        <w:LsdException Locked='false' Priority='61' Name='Light List Accent 2'/>
        <w:LsdException Locked='false' Priority='62' Name='Light Grid Accent 2'/>
        <w:LsdException Locked='false' Priority='63' Name='Medium Shading 1 Accent 2'/>
        <w:LsdException Locked='false' Priority='64' Name='Medium Shading 2 Accent 2'/>
        <w:LsdException Locked='false' Priority='65' Name='Medium List 1 Accent 2'/>
        <w:LsdException Locked='false' Priority='66' Name='Medium List 2 Accent 2'/>
        <w:LsdException Locked='false' Priority='67' Name='Medium Grid 1 Accent 2'/>
        <w:LsdException Locked='false' Priority='68' Name='Medium Grid 2 Accent 2'/>
        <w:LsdException Locked='false' Priority='69' Name='Medium Grid 3 Accent 2'/>
        <w:LsdException Locked='false' Priority='70' Name='Dark List Accent 2'/>
        <w:LsdException Locked='false' Priority='71' Name='Colorful Shading Accent 2'/>
        <w:LsdException Locked='false' Priority='72' Name='Colorful List Accent 2'/>
        <w:LsdException Locked='false' Priority='73' Name='Colorful Grid Accent 2'/>
        <w:LsdException Locked='false' Priority='60' Name='Light Shading Accent 3'/>
        <w:LsdException Locked='false' Priority='61' Name='Light List Accent 3'/>
        <w:LsdException Locked='false' Priority='62' Name='Light Grid Accent 3'/>
        <w:LsdException Locked='false' Priority='63' Name='Medium Shading 1 Accent 3'/>
        <w:LsdException Locked='false' Priority='64' Name='Medium Shading 2 Accent 3'/>
        <w:LsdException Locked='false' Priority='65' Name='Medium List 1 Accent 3'/>
        <w:LsdException Locked='false' Priority='66' Name='Medium List 2 Accent 3'/>
        <w:LsdException Locked='false' Priority='67' Name='Medium Grid 1 Accent 3'/>
        <w:LsdException Locked='false' Priority='68' Name='Medium Grid 2 Accent 3'/>
        <w:LsdException Locked='false' Priority='69' Name='Medium Grid 3 Accent 3'/>
        <w:LsdException Locked='false' Priority='70' Name='Dark List Accent 3'/>
        <w:LsdException Locked='false' Priority='71' Name='Colorful Shading Accent 3'/>
        <w:LsdException Locked='false' Priority='72' Name='Colorful List Accent 3'/>
        <w:LsdException Locked='false' Priority='73' Name='Colorful Grid Accent 3'/>
        <w:LsdException Locked='false' Priority='60' Name='Light Shading Accent 4'/>
        <w:LsdException Locked='false' Priority='61' Name='Light List Accent 4'/>
        <w:LsdException Locked='false' Priority='62' Name='Light Grid Accent 4'/>
        <w:LsdException Locked='false' Priority='63' Name='Medium Shading 1 Accent 4'/>
        <w:LsdException Locked='false' Priority='64' Name='Medium Shading 2 Accent 4'/>
        <w:LsdException Locked='false' Priority='65' Name='Medium List 1 Accent 4'/>
        <w:LsdException Locked='false' Priority='66' Name='Medium List 2 Accent 4'/>
        <w:LsdException Locked='false' Priority='67' Name='Medium Grid 1 Accent 4'/>
        <w:LsdException Locked='false' Priority='68' Name='Medium Grid 2 Accent 4'/>
        <w:LsdException Locked='false' Priority='69' Name='Medium Grid 3 Accent 4'/>
        <w:LsdException Locked='false' Priority='70' Name='Dark List Accent 4'/>
        <w:LsdException Locked='false' Priority='71' Name='Colorful Shading Accent 4'/>
        <w:LsdException Locked='false' Priority='72' Name='Colorful List Accent 4'/>
        <w:LsdException Locked='false' Priority='73' Name='Colorful Grid Accent 4'/>
        <w:LsdException Locked='false' Priority='60' Name='Light Shading Accent 5'/>
        <w:LsdException Locked='false' Priority='61' Name='Light List Accent 5'/>
        <w:LsdException Locked='false' Priority='62' Name='Light Grid Accent 5'/>
        <w:LsdException Locked='false' Priority='63' Name='Medium Shading 1 Accent 5'/>
        <w:LsdException Locked='false' Priority='64' Name='Medium Shading 2 Accent 5'/>
        <w:LsdException Locked='false' Priority='65' Name='Medium List 1 Accent 5'/>
        <w:LsdException Locked='false' Priority='66' Name='Medium List 2 Accent 5'/>
        <w:LsdException Locked='false' Priority='67' Name='Medium Grid 1 Accent 5'/>
        <w:LsdException Locked='false' Priority='68' Name='Medium Grid 2 Accent 5'/>
        <w:LsdException Locked='false' Priority='69' Name='Medium Grid 3 Accent 5'/>
        <w:LsdException Locked='false' Priority='70' Name='Dark List Accent 5'/>
        <w:LsdException Locked='false' Priority='71' Name='Colorful Shading Accent 5'/>
        <w:LsdException Locked='false' Priority='72' Name='Colorful List Accent 5'/>
        <w:LsdException Locked='false' Priority='73' Name='Colorful Grid Accent 5'/>
        <w:LsdException Locked='false' Priority='60' Name='Light Shading Accent 6'/>
        <w:LsdException Locked='false' Priority='61' Name='Light List Accent 6'/>
        <w:LsdException Locked='false' Priority='62' Name='Light Grid Accent 6'/>
        <w:LsdException Locked='false' Priority='63' Name='Medium Shading 1 Accent 6'/>
        <w:LsdException Locked='false' Priority='64' Name='Medium Shading 2 Accent 6'/>
        <w:LsdException Locked='false' Priority='65' Name='Medium List 1 Accent 6'/>
        <w:LsdException Locked='false' Priority='66' Name='Medium List 2 Accent 6'/>
        <w:LsdException Locked='false' Priority='67' Name='Medium Grid 1 Accent 6'/>
        <w:LsdException Locked='false' Priority='68' Name='Medium Grid 2 Accent 6'/>
        <w:LsdException Locked='false' Priority='69' Name='Medium Grid 3 Accent 6'/>
        <w:LsdException Locked='false' Priority='70' Name='Dark List Accent 6'/>
        <w:LsdException Locked='false' Priority='71' Name='Colorful Shading Accent 6'/>
        <w:LsdException Locked='false' Priority='72' Name='Colorful List Accent 6'/>
        <w:LsdException Locked='false' Priority='73' Name='Colorful Grid Accent 6'/>
        <w:LsdException Locked='false' Priority='19' QFormat='true'
        Name='Subtle Emphasis'/>
        <w:LsdException Locked='false' Priority='21' QFormat='true'
        Name='Intense Emphasis'/>
        <w:LsdException Locked='false' Priority='31' QFormat='true'
        Name='Subtle Reference'/>
        <w:LsdException Locked='false' Priority='32' QFormat='true'
        Name='Intense Reference'/>
        <w:LsdException Locked='false' Priority='33' QFormat='true' Name='Book Title'/>
        <w:LsdException Locked='false' Priority='37' SemiHidden='true'
        UnhideWhenUsed='true' Name='Bibliography'/>
        <w:LsdException Locked='false' Priority='39' SemiHidden='true'
        UnhideWhenUsed='true' QFormat='true' Name='TOC Heading'/>
        <w:LsdException Locked='false' Priority='41' Name='Plain Table 1'/>
        <w:LsdException Locked='false' Priority='42' Name='Plain Table 2'/>
        <w:LsdException Locked='false' Priority='43' Name='Plain Table 3'/>
        <w:LsdException Locked='false' Priority='44' Name='Plain Table 4'/>
        <w:LsdException Locked='false' Priority='45' Name='Plain Table 5'/>
        <w:LsdException Locked='false' Priority='40' Name='Grid Table Light'/>
        <w:LsdException Locked='false' Priority='46' Name='Grid Table 1 Light'/>
        <w:LsdException Locked='false' Priority='47' Name='Grid Table 2'/>
        <w:LsdException Locked='false' Priority='48' Name='Grid Table 3'/>
        <w:LsdException Locked='false' Priority='49' Name='Grid Table 4'/>
        <w:LsdException Locked='false' Priority='50' Name='Grid Table 5 Dark'/>
        <w:LsdException Locked='false' Priority='51' Name='Grid Table 6 Colorful'/>
        <w:LsdException Locked='false' Priority='52' Name='Grid Table 7 Colorful'/>
        <w:LsdException Locked='false' Priority='46'
        Name='Grid Table 1 Light Accent 1'/>
        <w:LsdException Locked='false' Priority='47' Name='Grid Table 2 Accent 1'/>
        <w:LsdException Locked='false' Priority='48' Name='Grid Table 3 Accent 1'/>
        <w:LsdException Locked='false' Priority='49' Name='Grid Table 4 Accent 1'/>
        <w:LsdException Locked='false' Priority='50' Name='Grid Table 5 Dark Accent 1'/>
        <w:LsdException Locked='false' Priority='51'
        Name='Grid Table 6 Colorful Accent 1'/>
        <w:LsdException Locked='false' Priority='52'
        Name='Grid Table 7 Colorful Accent 1'/>
        <w:LsdException Locked='false' Priority='46'
        Name='Grid Table 1 Light Accent 2'/>
        <w:LsdException Locked='false' Priority='47' Name='Grid Table 2 Accent 2'/>
        <w:LsdException Locked='false' Priority='48' Name='Grid Table 3 Accent 2'/>
        <w:LsdException Locked='false' Priority='49' Name='Grid Table 4 Accent 2'/>
        <w:LsdException Locked='false' Priority='50' Name='Grid Table 5 Dark Accent 2'/>
        <w:LsdException Locked='false' Priority='51'
        Name='Grid Table 6 Colorful Accent 2'/>
        <w:LsdException Locked='false' Priority='52'
        Name='Grid Table 7 Colorful Accent 2'/>
        <w:LsdException Locked='false' Priority='46'
        Name='Grid Table 1 Light Accent 3'/>
        <w:LsdException Locked='false' Priority='47' Name='Grid Table 2 Accent 3'/>
        <w:LsdException Locked='false' Priority='48' Name='Grid Table 3 Accent 3'/>
        <w:LsdException Locked='false' Priority='49' Name='Grid Table 4 Accent 3'/>
        <w:LsdException Locked='false' Priority='50' Name='Grid Table 5 Dark Accent 3'/>
        <w:LsdException Locked='false' Priority='51'
        Name='Grid Table 6 Colorful Accent 3'/>
        <w:LsdException Locked='false' Priority='52'
        Name='Grid Table 7 Colorful Accent 3'/>
        <w:LsdException Locked='false' Priority='46'
        Name='Grid Table 1 Light Accent 4'/>
        <w:LsdException Locked='false' Priority='47' Name='Grid Table 2 Accent 4'/>
        <w:LsdException Locked='false' Priority='48' Name='Grid Table 3 Accent 4'/>
        <w:LsdException Locked='false' Priority='49' Name='Grid Table 4 Accent 4'/>
        <w:LsdException Locked='false' Priority='50' Name='Grid Table 5 Dark Accent 4'/>
        <w:LsdException Locked='false' Priority='51'
        Name='Grid Table 6 Colorful Accent 4'/>
        <w:LsdException Locked='false' Priority='52'
        Name='Grid Table 7 Colorful Accent 4'/>
        <w:LsdException Locked='false' Priority='46'
        Name='Grid Table 1 Light Accent 5'/>
        <w:LsdException Locked='false' Priority='47' Name='Grid Table 2 Accent 5'/>
        <w:LsdException Locked='false' Priority='48' Name='Grid Table 3 Accent 5'/>
        <w:LsdException Locked='false' Priority='49' Name='Grid Table 4 Accent 5'/>
        <w:LsdException Locked='false' Priority='50' Name='Grid Table 5 Dark Accent 5'/>
        <w:LsdException Locked='false' Priority='51'
        Name='Grid Table 6 Colorful Accent 5'/>
        <w:LsdException Locked='false' Priority='52'
        Name='Grid Table 7 Colorful Accent 5'/>
        <w:LsdException Locked='false' Priority='46'
        Name='Grid Table 1 Light Accent 6'/>
        <w:LsdException Locked='false' Priority='47' Name='Grid Table 2 Accent 6'/>
        <w:LsdException Locked='false' Priority='48' Name='Grid Table 3 Accent 6'/>
        <w:LsdException Locked='false' Priority='49' Name='Grid Table 4 Accent 6'/>
        <w:LsdException Locked='false' Priority='50' Name='Grid Table 5 Dark Accent 6'/>
        <w:LsdException Locked='false' Priority='51'
        Name='Grid Table 6 Colorful Accent 6'/>
        <w:LsdException Locked='false' Priority='52'
        Name='Grid Table 7 Colorful Accent 6'/>
        <w:LsdException Locked='false' Priority='46' Name='List Table 1 Light'/>
        <w:LsdException Locked='false' Priority='47' Name='List Table 2'/>
        <w:LsdException Locked='false' Priority='48' Name='List Table 3'/>
        <w:LsdException Locked='false' Priority='49' Name='List Table 4'/>
        <w:LsdException Locked='false' Priority='50' Name='List Table 5 Dark'/>
        <w:LsdException Locked='false' Priority='51' Name='List Table 6 Colorful'/>
        <w:LsdException Locked='false' Priority='52' Name='List Table 7 Colorful'/>
        <w:LsdException Locked='false' Priority='46'
        Name='List Table 1 Light Accent 1'/>
        <w:LsdException Locked='false' Priority='47' Name='List Table 2 Accent 1'/>
        <w:LsdException Locked='false' Priority='48' Name='List Table 3 Accent 1'/>
        <w:LsdException Locked='false' Priority='49' Name='List Table 4 Accent 1'/>
        <w:LsdException Locked='false' Priority='50' Name='List Table 5 Dark Accent 1'/>
        <w:LsdException Locked='false' Priority='51'
        Name='List Table 6 Colorful Accent 1'/>
        <w:LsdException Locked='false' Priority='52'
        Name='List Table 7 Colorful Accent 1'/>
        <w:LsdException Locked='false' Priority='46'
        Name='List Table 1 Light Accent 2'/>
        <w:LsdException Locked='false' Priority='47' Name='List Table 2 Accent 2'/>
        <w:LsdException Locked='false' Priority='48' Name='List Table 3 Accent 2'/>
        <w:LsdException Locked='false' Priority='49' Name='List Table 4 Accent 2'/>
        <w:LsdException Locked='false' Priority='50' Name='List Table 5 Dark Accent 2'/>
        <w:LsdException Locked='false' Priority='51'
        Name='List Table 6 Colorful Accent 2'/>
        <w:LsdException Locked='false' Priority='52'
        Name='List Table 7 Colorful Accent 2'/>
        <w:LsdException Locked='false' Priority='46'
        Name='List Table 1 Light Accent 3'/>
        <w:LsdException Locked='false' Priority='47' Name='List Table 2 Accent 3'/>
        <w:LsdException Locked='false' Priority='48' Name='List Table 3 Accent 3'/>
        <w:LsdException Locked='false' Priority='49' Name='List Table 4 Accent 3'/>
        <w:LsdException Locked='false' Priority='50' Name='List Table 5 Dark Accent 3'/>
        <w:LsdException Locked='false' Priority='51'
        Name='List Table 6 Colorful Accent 3'/>
        <w:LsdException Locked='false' Priority='52'
        Name='List Table 7 Colorful Accent 3'/>
        <w:LsdException Locked='false' Priority='46'
        Name='List Table 1 Light Accent 4'/>
        <w:LsdException Locked='false' Priority='47' Name='List Table 2 Accent 4'/>
        <w:LsdException Locked='false' Priority='48' Name='List Table 3 Accent 4'/>
        <w:LsdException Locked='false' Priority='49' Name='List Table 4 Accent 4'/>
        <w:LsdException Locked='false' Priority='50' Name='List Table 5 Dark Accent 4'/>
        <w:LsdException Locked='false' Priority='51'
        Name='List Table 6 Colorful Accent 4'/>
        <w:LsdException Locked='false' Priority='52'
        Name='List Table 7 Colorful Accent 4'/>
        <w:LsdException Locked='false' Priority='46'
        Name='List Table 1 Light Accent 5'/>
        <w:LsdException Locked='false' Priority='47' Name='List Table 2 Accent 5'/>
        <w:LsdException Locked='false' Priority='48' Name='List Table 3 Accent 5'/>
        <w:LsdException Locked='false' Priority='49' Name='List Table 4 Accent 5'/>
        <w:LsdException Locked='false' Priority='50' Name='List Table 5 Dark Accent 5'/>
        <w:LsdException Locked='false' Priority='51'
        Name='List Table 6 Colorful Accent 5'/>
        <w:LsdException Locked='false' Priority='52'
        Name='List Table 7 Colorful Accent 5'/>
        <w:LsdException Locked='false' Priority='46'
        Name='List Table 1 Light Accent 6'/>
        <w:LsdException Locked='false' Priority='47' Name='List Table 2 Accent 6'/>
        <w:LsdException Locked='false' Priority='48' Name='List Table 3 Accent 6'/>
        <w:LsdException Locked='false' Priority='49' Name='List Table 4 Accent 6'/>
        <w:LsdException Locked='false' Priority='50' Name='List Table 5 Dark Accent 6'/>
        <w:LsdException Locked='false' Priority='51'
        Name='List Table 6 Colorful Accent 6'/>
        <w:LsdException Locked='false' Priority='52'
        Name='List Table 7 Colorful Accent 6'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Mention'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Smart Hyperlink'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Hashtag'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Unresolved Mention'/>
        <w:LsdException Locked='false' SemiHidden='true' UnhideWhenUsed='true'
        Name='Smart Link'/>
        </w:LatentStyles>
        </xml><![endif]-->
        <style>
        <!--
        /* Font Definitions */
        @font-face
            {font-family:'Cambria Math';
            panose-1:2 4 5 3 5 4 6 3 2 4;
            mso-font-charset:0;
            mso-generic-font-family:roman;
            mso-font-pitch:variable;
            mso-font-signature:-536869121 1107305727 33554432 0 415 0;}
        @font-face
            {font-family:'Noto Sans Arabic';
            panose-1:0 0 0 0 0 0 0 0 0 0;
            mso-font-alt:Calibri;
            mso-font-charset:0;
            mso-generic-font-family:auto;
            mso-font-format:other;
            mso-font-pitch:auto;
            mso-font-signature:3 0 0 0 1 0;}
        /* Style Definitions */
        p.MsoNormal, li.MsoNormal, div.MsoNormal
            {mso-style-unhide:no;
            mso-style-qformat:yes;
            mso-style-parent:'';
            margin:0cm;
            line-height:115%;
            mso-pagination:widow-orphan;
            font-size:13.0pt;
            font-family:'Arial',sans-serif;
            mso-fareast-font-family:'Times New Roman';
            mso-ansi-language:EN-GB;}
        h1
            {mso-style-priority:9;
            mso-style-unhide:no;
            mso-style-qformat:yes;
            mso-style-link:'Heading 1 Char';
            mso-style-next:Normal;
            margin-top:20.0pt;
            margin-right:0cm;
            margin-bottom:6.0pt;
            margin-left:0cm;
            line-height:115%;
            mso-pagination:widow-orphan lines-together;
            page-break-after:avoid;
            mso-outline-level:1;
            font-size:20.0pt;
            font-family:'Arial',sans-serif;
            mso-font-kerning:0pt;
            mso-ansi-language:EN-GB;
            font-weight:normal;}
        h2
            {mso-style-noshow:yes;
            mso-style-priority:9;
            mso-style-qformat:yes;
            mso-style-link:'Heading 2 Char';
            mso-style-next:Normal;
            margin-top:18.0pt;
            margin-right:0cm;
            margin-bottom:6.0pt;
            margin-left:0cm;
            line-height:115%;
            mso-pagination:widow-orphan lines-together;
            page-break-after:avoid;
            mso-outline-level:2;
            font-size:16.0pt;
            font-family:'Arial',sans-serif;
            mso-ansi-language:EN-GB;
            font-weight:normal;}
        h3
            {mso-style-noshow:yes;
            mso-style-priority:9;
            mso-style-qformat:yes;
            mso-style-link:'Heading 3 Char';
            mso-style-next:Normal;
            margin-top:16.0pt;
            margin-right:0cm;
            margin-bottom:4.0pt;
            margin-left:0cm;
            line-height:115%;
            mso-pagination:widow-orphan lines-together;
            page-break-after:avoid;
            mso-outline-level:3;
            font-size:14.0pt;
            font-family:'Arial',sans-serif;
            color:#434343;
            mso-ansi-language:EN-GB;
            font-weight:normal;}
        h4
            {mso-style-noshow:yes;
            mso-style-priority:9;
            mso-style-qformat:yes;
            mso-style-link:'Heading 4 Char';
            mso-style-next:Normal;
            margin-top:14.0pt;
            margin-right:0cm;
            margin-bottom:4.0pt;
            margin-left:0cm;
            line-height:115%;
            mso-pagination:widow-orphan lines-together;
            page-break-after:avoid;
            mso-outline-level:4;
            font-size:12.0pt;
            font-family:'Arial',sans-serif;
            color:#666666;
            mso-ansi-language:EN-GB;
            font-weight:normal;}
        h5
            {mso-style-noshow:yes;
            mso-style-priority:9;
            mso-style-qformat:yes;
            mso-style-link:'Heading 5 Char';
            mso-style-next:Normal;
            margin-top:12.0pt;
            margin-right:0cm;
            margin-bottom:4.0pt;
            margin-left:0cm;
            line-height:115%;
            mso-pagination:widow-orphan lines-together;
            page-break-after:avoid;
            mso-outline-level:5;
            font-size:13.0pt;
            font-family:'Arial',sans-serif;
            color:#666666;
            mso-ansi-language:EN-GB;
            font-weight:normal;}
        h6
            {mso-style-noshow:yes;
            mso-style-priority:9;
            mso-style-qformat:yes;
            mso-style-link:'Heading 6 Char';
            mso-style-next:Normal;
            margin-top:12.0pt;
            margin-right:0cm;
            margin-bottom:4.0pt;
            margin-left:0cm;
            line-height:115%;
            mso-pagination:widow-orphan lines-together;
            page-break-after:avoid;
            mso-outline-level:6;
            font-size:13.0pt;
            font-family:'Arial',sans-serif;
            color:#666666;
            mso-ansi-language:EN-GB;
            font-weight:normal;
            font-style:italic;
            mso-bidi-font-style:normal;}
        p.MsoTitle, li.MsoTitle, div.MsoTitle
            {mso-style-priority:10;
            mso-style-unhide:no;
            mso-style-qformat:yes;
            mso-style-link:'Title Char';
            mso-style-next:Normal;
            margin-top:0cm;
            margin-right:0cm;
            margin-bottom:3.0pt;
            margin-left:0cm;
            line-height:115%;
            mso-pagination:widow-orphan lines-together;
            page-break-after:avoid;
            font-size:26.0pt;
            font-family:'Arial',sans-serif;
            mso-fareast-font-family:'Times New Roman';
            mso-ansi-language:EN-GB;}
        p.MsoSubtitle, li.MsoSubtitle, div.MsoSubtitle
            {mso-style-priority:11;
            mso-style-unhide:no;
            mso-style-qformat:yes;
            mso-style-link:'Subtitle Char';
            mso-style-next:Normal;
            margin-top:0cm;
            margin-right:0cm;
            margin-bottom:16.0pt;
            margin-left:0cm;
            line-height:115%;
            mso-pagination:widow-orphan lines-together;
            page-break-after:avoid;
            font-size:15.0pt;
            font-family:'Arial',sans-serif;
            mso-fareast-font-family:'Times New Roman';
            color:#666666;
            mso-ansi-language:EN-GB;}
        p
            {mso-style-noshow:yes;
            mso-style-priority:99;
            mso-margin-top-alt:auto;
            margin-right:0cm;
            mso-margin-bottom-alt:auto;
            margin-left:0cm;
            mso-pagination:widow-orphan;
            font-size:12.0pt;
            font-family:'Times New Roman',serif;
            mso-fareast-font-family:'Times New Roman';}
        span.Heading1Char
            {mso-style-name:'Heading 1 Char';
            mso-style-priority:9;
            mso-style-unhide:no;
            mso-style-locked:yes;
            mso-style-link:'Heading 1';
            mso-ansi-font-size:16.0pt;
            mso-bidi-font-size:16.0pt;
            font-family:'Calibri Light',sans-serif;
            mso-ascii-font-family:'Calibri Light';
            mso-ascii-theme-font:major-latin;
            mso-fareast-font-family:'Times New Roman';
            mso-fareast-theme-font:major-fareast;
            mso-hansi-font-family:'Calibri Light';
            mso-hansi-theme-font:major-latin;
            mso-bidi-font-family:'Times New Roman';
            mso-font-kerning:16.0pt;
            font-weight:bold;}
        span.Heading2Char
            {mso-style-name:'Heading 2 Char';
            mso-style-noshow:yes;
            mso-style-priority:9;
            mso-style-unhide:no;
            mso-style-locked:yes;
            mso-style-link:'Heading 2';
            mso-ansi-font-size:14.0pt;
            mso-bidi-font-size:14.0pt;
            font-family:'Calibri Light',sans-serif;
            mso-ascii-font-family:'Calibri Light';
            mso-ascii-theme-font:major-latin;
            mso-fareast-font-family:'Times New Roman';
            mso-fareast-theme-font:major-fareast;
            mso-hansi-font-family:'Calibri Light';
            mso-hansi-theme-font:major-latin;
            mso-bidi-font-family:'Times New Roman';
            font-weight:bold;
            font-style:italic;}
        span.Heading3Char
            {mso-style-name:'Heading 3 Char';
            mso-style-noshow:yes;
            mso-style-priority:9;
            mso-style-unhide:no;
            mso-style-locked:yes;
            mso-style-link:'Heading 3';
            mso-ansi-font-size:13.0pt;
            mso-bidi-font-size:13.0pt;
            font-family:'Calibri Light',sans-serif;
            mso-ascii-font-family:'Calibri Light';
            mso-ascii-theme-font:major-latin;
            mso-fareast-font-family:'Times New Roman';
            mso-fareast-theme-font:major-fareast;
            mso-hansi-font-family:'Calibri Light';
            mso-hansi-theme-font:major-latin;
            mso-bidi-font-family:'Times New Roman';
            font-weight:bold;}
        span.Heading4Char
            {mso-style-name:'Heading 4 Char';
            mso-style-noshow:yes;
            mso-style-priority:9;
            mso-style-unhide:no;
            mso-style-locked:yes;
            mso-style-link:'Heading 4';
            mso-ansi-font-size:14.0pt;
            mso-bidi-font-size:14.0pt;
            font-family:'Calibri',sans-serif;
            mso-ascii-font-family:Calibri;
            mso-ascii-theme-font:minor-latin;
            mso-fareast-font-family:'Times New Roman';
            mso-fareast-theme-font:minor-fareast;
            mso-hansi-font-family:Calibri;
            mso-hansi-theme-font:minor-latin;
            mso-bidi-font-family:'Times New Roman';
            font-weight:bold;}
        span.Heading5Char
            {mso-style-name:'Heading 5 Char';
            mso-style-noshow:yes;
            mso-style-priority:9;
            mso-style-unhide:no;
            mso-style-locked:yes;
            mso-style-link:'Heading 5';
            mso-ansi-font-size:13.0pt;
            mso-bidi-font-size:13.0pt;
            font-family:'Calibri',sans-serif;
            mso-ascii-font-family:Calibri;
            mso-ascii-theme-font:minor-latin;
            mso-fareast-font-family:'Times New Roman';
            mso-fareast-theme-font:minor-fareast;
            mso-hansi-font-family:Calibri;
            mso-hansi-theme-font:minor-latin;
            mso-bidi-font-family:'Times New Roman';
            font-weight:bold;
            font-style:italic;}
        span.Heading6Char
            {mso-style-name:'Heading 6 Char';
            mso-style-noshow:yes;
            mso-style-priority:9;
            mso-style-unhide:no;
            mso-style-locked:yes;
            mso-style-link:'Heading 6';
            font-family:'Calibri',sans-serif;
            mso-ascii-font-family:Calibri;
            mso-ascii-theme-font:minor-latin;
            mso-fareast-font-family:'Times New Roman';
            mso-fareast-theme-font:minor-fareast;
            mso-hansi-font-family:Calibri;
            mso-hansi-theme-font:minor-latin;
            mso-bidi-font-family:'Times New Roman';
            font-weight:bold;}
        span.TitleChar
            {mso-style-name:'Title Char';
            mso-style-priority:10;
            mso-style-unhide:no;
            mso-style-locked:yes;
            mso-style-link:Title;
            mso-ansi-font-size:16.0pt;
            mso-bidi-font-size:16.0pt;
            font-family:'Calibri Light',sans-serif;
            mso-ascii-font-family:'Calibri Light';
            mso-ascii-theme-font:major-latin;
            mso-fareast-font-family:'Times New Roman';
            mso-fareast-theme-font:major-fareast;
            mso-hansi-font-family:'Calibri Light';
            mso-hansi-theme-font:major-latin;
            mso-bidi-font-family:'Times New Roman';
            mso-font-kerning:14.0pt;
            font-weight:bold;}
        span.SubtitleChar
            {mso-style-name:'Subtitle Char';
            mso-style-priority:11;
            mso-style-unhide:no;
            mso-style-locked:yes;
            mso-style-link:Subtitle;
            mso-ansi-font-size:12.0pt;
            mso-bidi-font-size:12.0pt;
            font-family:'Calibri Light',sans-serif;
            mso-ascii-font-family:'Calibri Light';
            mso-ascii-theme-font:major-latin;
            mso-fareast-font-family:'Times New Roman';
            mso-fareast-theme-font:major-fareast;
            mso-hansi-font-family:'Calibri Light';
            mso-hansi-theme-font:major-latin;
            mso-bidi-font-family:'Times New Roman';}
        .MsoChpDefault
            {mso-style-type:export-only;
            mso-default-props:yes;
            font-family:'Arial',sans-serif;
            mso-ascii-font-family:Arial;
            mso-hansi-font-family:Arial;
            mso-bidi-font-family:Arial;
            mso-ansi-language:EN-GB;}
        .MsoPapDefault
            {mso-style-type:export-only;
            line-height:115%;}
        @page WordSection1
            {size:595.45pt 841.7pt;
            margin:70.85pt 2.0cm 2.0cm 2.0cm;
            mso-header-margin:36.0pt;
            mso-footer-margin:36.0pt;
            mso-page-numbers:1;
            mso-paper-source:0;}
        div.WordSection1
            {page:WordSection1;}
        /* List Definitions */
        @list l0
            {mso-list-id:1414619638;
            mso-list-template-ids:-891647312;}
        @list l0:level1
            {mso-level-number-format:bullet;
            mso-level-text:\25CF;
            mso-level-tab-stop:none;
            mso-level-number-position:left;
            text-indent:-18.0pt;
            text-decoration:none;
            text-underline:none;}
        @list l0:level2
            {mso-level-number-format:bullet;
            mso-level-text:\25CB;
            mso-level-tab-stop:none;
            mso-level-number-position:left;
            text-indent:-18.0pt;
            text-decoration:none;
            text-underline:none;}
        @list l0:level3
            {mso-level-number-format:bullet;
            mso-level-text:\25A0;
            mso-level-tab-stop:none;
            mso-level-number-position:left;
            text-indent:-18.0pt;
            text-decoration:none;
            text-underline:none;}
        @list l0:level4
            {mso-level-number-format:bullet;
            mso-level-text:\25CF;
            mso-level-tab-stop:none;
            mso-level-number-position:left;
            text-indent:-18.0pt;
            text-decoration:none;
            text-underline:none;}
        @list l0:level5
            {mso-level-number-format:bullet;
            mso-level-text:\25CB;
            mso-level-tab-stop:none;
            mso-level-number-position:left;
            text-indent:-18.0pt;
            text-decoration:none;
            text-underline:none;}
        @list l0:level6
            {mso-level-number-format:bullet;
            mso-level-text:\25A0;
            mso-level-tab-stop:none;
            mso-level-number-position:left;
            text-indent:-18.0pt;
            text-decoration:none;
            text-underline:none;}
        @list l0:level7
            {mso-level-number-format:bullet;
            mso-level-text:\25CF;
            mso-level-tab-stop:none;
            mso-level-number-position:left;
            text-indent:-18.0pt;
            text-decoration:none;
            text-underline:none;}
        @list l0:level8
            {mso-level-number-format:bullet;
            mso-level-text:\25CB;
            mso-level-tab-stop:none;
            mso-level-number-position:left;
            text-indent:-18.0pt;
            text-decoration:none;
            text-underline:none;}
        @list l0:level9
            {mso-level-number-format:bullet;
            mso-level-text:\25A0;
            mso-level-tab-stop:none;
            mso-level-number-position:left;
            text-indent:-18.0pt;
            text-decoration:none;
            text-underline:none;}
        ol
            {margin-bottom:0cm;}
        ul
            {margin-bottom:0cm;}
        -->
        </style>
        <!--[if gte mso 10]>
        <style>
        /* Style Definitions */
        table.MsoNormalTable
            {mso-style-name:'Table Normal';
            mso-tstyle-rowband-size:0;
            mso-tstyle-colband-size:0;
            mso-style-noshow:yes;
            mso-style-priority:99;
            mso-style-parent:'';
            mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
            mso-para-margin:0cm;
            line-height:115%;
            mso-pagination:widow-orphan;
            font-size:13.0pt;
            font-family:'Arial',sans-serif;
            mso-ansi-language:EN-GB;}
        </style>
        <![endif]--><!--[if gte mso 9]><xml>
        <o:shapedefaults v:ext='edit' spidmax='1026'/>
        </xml><![endif]--><!--[if gte mso 9]><xml>
        <o:shapelayout v:ext='edit'>
        <o:idmap v:ext='edit' data='1'/>
        </o:shapelayout></xml><![endif]-->
        </head>

        <body lang=IT style='tab-interval:36.0pt;word-wrap:break-word'>

        <div class=WordSection1>

        <p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-GB
        style='font-size:24.0pt;line-height:115%;font-family:'Noto Sans Arabic';
        mso-bidi-font-family:'Noto Sans Arabic''>DNAI Analysis<i style='mso-bidi-font-style:
        normal'>""" + f"""
        #{str(count)}</i></span></b><b style='mso-bidi-font-weight:normal'><i
        style='mso-bidi-font-style:normal'><span lang=EN-GB style='font-size:6.0pt;
        line-height:115%;font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic''><o:p></o:p></span></i></b></p>

        <div class=MsoNormal align=center style='text-align:center'><span lang=EN-GB>

        <hr size=2 width='100%' align=center>

        </span></div>

        <p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-GB
        style='font-size:1.0pt;line-height:115%;font-family:'Noto Sans Arabic';
        mso-bidi-font-family:'Noto Sans Arabic''><o:p>&nbsp;</o:p></span></b></p>

        <p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-GB
        style='font-size:1.0pt;line-height:115%;font-family:'Noto Sans Arabic';
        mso-bidi-font-family:'Noto Sans Arabic''><o:p>&nbsp;</o:p></span></b></p>

        <p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-GB
        style='font-size:1.0pt;line-height:115%;font-family:'Noto Sans Arabic';
        mso-bidi-font-family:'Noto Sans Arabic''><o:p>&nbsp;</o:p></span></b></p>

        <p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN-GB
        style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic''><o:p>&nbsp;</o:p></span></i></p>

        <p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN-GB
        style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic''>Dear
        Patient,<o:p></o:p></span></i></p>

        <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
        mso-bidi-font-family:'Noto Sans Arabic''>We hope this report finds you in good
        health. The purpose of this correspondence is to communicate the findings of
        the genetic analysis conducted by the DNAI research team using artificial
        intelligence (AI). Your participation in this study has been invaluable,
        contributing significantly to the progress of genetic research.<o:p></o:p></span></p>

        <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
        mso-bidi-font-family:'Noto Sans Arabic''><o:p>&nbsp;</o:p></span></p>

        <p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-GB
        style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic''>INTRODUCTION:<o:p></o:p></span></b></p>

        <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
        mso-bidi-font-family:'Noto Sans Arabic''>The DNAI research team, in
        collaboration with cutting-edge technology experts, has employed a
        state-of-the-art machine learning model to conduct a comprehensive analysis of
        your genetic information. The primary objective was to identify potential
        genetic anomalies and assess the risk of specific genetic diseases.<o:p></o:p></span></p>

        <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
        mso-bidi-font-family:'Noto Sans Arabic''><o:p>&nbsp;</o:p></span></p>

        <p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-GB
        style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic''>RESULTS:<o:p></o:p></span></b></p>
        
        """ 
    )

    for k,j in enumerate(genetic_markers):
        if k > 0:
            new_lines.append(f"""
                 <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
                mso-bidi-font-family:'Noto Sans Arabic''>Furthermore you also have been diagnosed with <strong>{disorder[k].lower()}</strong> which means as follows:<o:p></o:p></span></p>          
            """)
        else:
            new_lines.append(f"""
                <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
                mso-bidi-font-family:'Noto Sans Arabic''>Following an extensive examination,
                the outcomes of the genetic analysis are that you have been diagnosed with <strong>{disorder[k].lower()}</strong> which means as follows:<o:p></o:p></span></p>                 
            """)

        new_lines.append(f"""
            <p class=MsoNormal style='margin-left:36.0pt;text-indent:-18.0pt;mso-list:l0 level1 lfo1'><![if !supportLists]><span
            lang=EN-GB style='font-family:'Noto Sans Arabic';mso-fareast-font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic''><span style='mso-list:Ignore'>&#9679;<span
            style='font:7.0pt 'Times New Roman''>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </span></span></span><![endif]><span lang=EN-GB style='font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic''>Genetic Markers: {genetic_markers[k]}<o:p></o:p></span></p>

            <p class=MsoNormal style='margin-left:36.0pt;text-indent:-18.0pt;mso-list:l0 level1 lfo1'><![if !supportLists]><span
            lang=EN-GB style='font-family:'Noto Sans Arabic';mso-fareast-font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic''><span style='mso-list:Ignore'>&#9679;<span
            style='font:7.0pt 'Times New Roman''>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </span></span></span><![endif]><span lang=EN-GB style='font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic''>Risk Factors: {risk_factors[k]}<o:p></o:p></span></p>

            <p class=MsoNormal style='margin-left:36.0pt;text-indent:-18.0pt;mso-list:l0 level1 lfo1'><![if !supportLists]><span
            lang=EN-GB style='font-family:'Noto Sans Arabic';mso-fareast-font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic''><span style='mso-list:Ignore'>&#9679;<span
            style='font:7.0pt 'Times New Roman''>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </span></span></span><![endif]><span lang=EN-GB style='font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic''>Recommendations: {recommendations[k]}<o:p></o:p></span></p>
            """
        )

    new_lines.append(f"""
            <p class=MsoNormal style='margin-left:36.0pt'><span lang=EN-GB
            style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic''><o:p>&nbsp;</o:p></span></p>

            <p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-GB
            style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic''>INTERPRETATION:<o:p></o:p></span></b></p>

            <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic''>It is crucial to interpret these
            results with caution. The information obtained is not deterministic but
            provides valuable insights into potential genetic predispositions. These
            findings should be discussed in consultation with a healthcare professional
            specializing in genetics to formulate an appropriate plan for further
            evaluation or monitoring.<o:p></o:p></span></p>

            <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic''><o:p>&nbsp;</o:p></span></p>

            <p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-GB
            style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic''>DISCUSSION:<o:p></o:p></span></b></p>

            <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic''>Our team is available to discuss the
            results in detail, address any questions or concerns you may have, and provide
            guidance on the implications of the findings. We recommend scheduling a
            follow-up appointment with a healthcare professional to ensure a comprehensive
            understanding of the results and to explore any necessary next steps.<o:p></o:p></span></p>

            <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic''><o:p>&nbsp;</o:p></span></p>

            <p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-GB
            style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic''>PATTERNS:</span></b><span
            lang=EN-GB style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic';
            mso-bidi-font-weight:bold'><br>
            In the context of genetic analysis using artificial intelligence (AI), patterns
            refer to recurring trends or structures in genetic data. During the AI training
            phase, the model learns patterns associated with genetic disorders from a
            dataset. When analysing new genetic samples, the model looks for similar
            patterns it learned during training to predict or detect the likelihood of a
            genetic disorder in the individual. The accuracy of the model depends on the
            quality of training data and the effectiveness of the machine learning
            algorithms.<o:p></o:p></span></p>

            <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic';mso-bidi-font-weight:bold'><o:p>&nbsp;</o:p></span></p>

            <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic';mso-bidi-font-weight:bold'>You will
            find the report of your sample in the next page, highlighted the anomalies that
            reconducted to the genetic disorder. Highlighted in orange are the the bases that showing no presence of any disease, in yellow representing lactose intolerance, in light blue haemophilia and light green autism </span><b style='mso-bidi-font-weight:
            normal'><span lang=EN-GB style='font-family:'Noto Sans Arabic';mso-bidi-font-family:
            'Noto Sans Arabic''><o:p></o:p></span></b></p>

            <p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-GB
            style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic''><o:p>&nbsp;</o:p></span></b></p>
            
            {patterns}

            <p class=MsoNormal><span lang=EN-GB style='font-family:'Noto Sans Arabic';
            mso-bidi-font-family:'Noto Sans Arabic''><o:p>&nbsp;</o:p></span></p>

            <p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN-GB
            style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic''>CONCLUSION:</span></b><span
            lang=EN-GB style='font-family:'Noto Sans Arabic';mso-bidi-font-family:'Noto Sans Arabic';
            mso-bidi-font-weight:bold'><br>
            Your health is paramount to us, and we remain committed to supporting you throughout this 
            process. Please do not hesitate to contact our team if you require additional
            information or wish to schedule a consultation. Thank you for your participation
            in this groundbreaking research endeavor. Your contribution has significantly
            contributed to the advancement of genetic medicine.<o:p></o:p></span></p>

            <p style='margin:0cm'><span lang=EN-US style='font-size:13.0pt;font-family:
            'Noto Sans Arabic';color:black;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

            <p style='margin:0cm'><span lang=EN-GB style='font-size:13.0pt;font-family:
            'Noto Sans Arabic';color:black;mso-ansi-language:EN-GB'>Sincerely,</span><span
            lang=EN-GB style='mso-ansi-language:EN-GB'><o:p></o:p></span></p>

            <p style='margin:0cm'><i><span lang=EN-GB style='font-size:13.0pt;font-family:
            'Noto Sans Arabic';color:black;mso-ansi-language:EN-GB'>The DNAI Team</span></i><span
            lang=EN-GB style='mso-ansi-language:EN-GB'><o:p></o:p></span></p>

            <p class=MsoNormal><span lang=EN-GB><o:p>&nbsp;</o:p></span></p>

            </div>

            </body>

            </html>

    """
    )

    html_code = ' '.join([str(i) for i in new_lines])

    convert_html_to_pdf(html_code, f'static/analysis/analysis_{str(count)}.pdf')