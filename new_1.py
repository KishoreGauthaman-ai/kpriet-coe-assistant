import pywhatkit
import time

# Example dictionary
place_phone_dict = {
    "Winner Medicals Store": "7200261300",
    "Liji Acupuncture clinic": "9095772231",
    "Sri Ramanuja Thayar Herbals": "9688489669",
    "N.S.E Dental Hospital": "9965421717",
    "Vishnu Clinic": "9629412349",
    "Visnuu's dental clinic": "7845219180",
    "DEV DENTAL HUB & ORTHODONTIC CENTRE": "9952824400",
    "Jawahar Clinic": "8870935466",
    "Wellness physio clinic": "6380788643",
    "Sana's beauty clinic": "9688815566",
    "Dr.Arunprasath's Homeopathy Clinic": "7092966977",
    "Acupuncture treatment": "9788810835",
    "Ara’s Rehab Center குழந்தைகள் மனநல மறுவாழ்வு மையம்": "9003531445",
    "MS CLINIC": "9360883095",
    "Ajaihomoeoclinic": "9443760319",
    "Mayura Dental Solution": "9514450854",
    "Sri Karunambikai Multispeciality Hospital & Maternity Centre~Advanced Fertility care & Scan centre 24x7Emergency care": "8148172898",
    "VEDHA DENTAL CLINIC 2": "8838239530",
    "Sri Sakthi Clinic": "4296274727",
    "Skandda Dental Center": "9442351339",
    "PODIPALAYAM VAITHYASALAI": "9944365098",
    "Aditya Health Center Avinashi": "9443760319",
    "PRIME MEDICAL CENTRE": "9894890049",
    "Podhini Siddha Clinic": "8220961323",
    "Krishna Ayurvedic clinic": "9597701606",
    "KUMARAN CLINIC": "9345204549",
    "SUBAM CLINIC": "9344574350",
    "Sri sakthi illam, Thodu sigichai Maiyam": "9842288750",
    "SAI KRISHNA CLINIC": "8056605201",
    "Rakshaen clinic": "9159147575",
    "Kalki Multispeciality Clinic": "8667222850",
    "Ayurveda & Panchakarma Therapy centre": "7708439406",
    "Anitha Speciality Clinic": "7550097809",
    "Anbu dental clinic (Root canal and implant center)": "8825817992",
    "Dr Kavin Prasad.S": "8270065644",
    "Senthur Dental Care செந்தூர் பல் மருத்துவமனை सेंथुर डेंटल हॉस्पिटल": "8270065644",
    "YA SHAFI HEALTH CARE": "8248794780",
    "AR DENTAL CLINIC& SMILE DESIGNER": "8300215670",
    "Sugam Health Center": "9360244874",
    "Siuly clinic": "9042706639",
    "NALAM HOMOEO CARE": "9363031936",
    "HYTEC SYSTEMS": "9790502720",
    "Yuva Medicals": "9361770843",
    "MM Dental Care": "9363738319",
    "Maragatham dental clinic |Invisible braces|Dental clinic Dharapuram |Root canal treatment |Dental implants|Laser": "9444284868",
    "Jayam Acupunture Dharapuram": "9047145403",
    "Himalaya physiotherapy & Chiropractic clinic Since 2009 | Physiotherapy Clinic in Dharapuram": "9865384288",
    "MAGHIL DENTAL CARE & IMPLANT CENTRE": "7449242526",
    "Raj Dental Clinic": "7904464627",
    "Meera Dental Clinic": "9962337424"
}

message_template = """
Hi {place},
   
I came across your clinic and noticed you don’t have a website yet. I wanted to share an idea — a professional website can help patients find your clinic easily, understand your services, and build more trust before visiting.

I create modern, mobile-friendly websites for clinics with service details, doctor information, location, and contact options.

I’d love to show you a simple demo idea of how your clinic’s website could look.

Thank you,
kishore
"""

for place, phone in place_phone_dict.items():

    # Remove spaces and +91 prefix
    clean_phone = phone.replace(" ", "").replace("+91", "")

    # Add country code back in the format required by WhatsApp API
    whatsapp_number = f"+91{clean_phone}"

    # Personalize message
    message = message_template.format(place=place)

    try:
        pywhatkit.sendwhatmsg_instantly(
            whatsapp_number,
            message,
            wait_time=15,
            tab_close=True,
            close_time=5
        )

        print(f"Message sent to {place} -> {whatsapp_number}")

        # Avoid sending too fast
        time.sleep(7)

    except Exception as e:
        print(f"Failed for {place}: {e}")