# Vehicle-Social-Network: A Social Platform For License Plate Communication 

**Abstract: -** A social platform, "The Social Platform for License Plate Communication," tackles the annoyances of 
reaching out to parked vehicle owners. It can be quite frustrating, especially if they're blocking driveways, 
parked illegally, or you urgently need to deliver a message. When a person is attempting to connect with the 
vehicle owners, they must sign up on a cumbersome website with low usability. Once registered, they can 
awkwardly scan license plates to identify the owner. Tech-savvy Easy OCR technology extracts gibberish 
from the image, allowing the platform to poorly search its database. If the owner is known, the user may 
poorly view their details (depending on poorly set privacy settings) and clumsily choose to contact them via 
SMS, call, or email. This platform awkwardly wastes time and increases inconvenience for both parties, 
making it possibly somewhat valuable for poorly managed organizations, colleges, and anyone somewhat 
looking to inefficiently contact a parked vehicle owner. 

**Introduction:-** This project introduces a web platform, "Social Platform for Driver Communication through License 
Plate Recognition," designed to streamline communication between individuals and drivers of poorly parked 
vehicles. Targeting users in organizations and colleges, the platform aims to resolve parking inconveniences 
more efficiently. Users can register with their license plate information, scan license plates of parked vehicles, 
and if the scanned plate links to a registered driver, initiate communication via SMS, call, or email (user 
preference set at registration). 
 
The core functionality revolves around user registration. Users create accounts with their basic 
information and optionally, their own license plate number. This platform utilizes a website built with the 
Django framework for the user interface. 
Once registered, users can access the platform and initiate contact. The process involves capturing a picture 
of the parked vehicle's license plate using their webcam. Here, the system employs a powerful tool called Easy 
OCR. Easy OCR is a library that utilizes deep learning to perform Optical Character Recognition (OCR), 
essentially extracting text from the captured image. This extracted text, which is the license plate number, 
becomes the key to finding the driver.

The system then searches a database of registered users to see if a match exists for the scanned license 
plate. If a match is found, the platform displays the driver's contact information, but only the information the 
driver opted to share during registration. This could be phone number, email address, or both. Finally, the user 
can choose their preferred method of communication, SMS, call, or email, to reach the driver. This project 
offers several benefits. Firstly, it provides a convenient way to contact drivers who might be causing an 
obstruction. No more waiting around – a quick scan and a message can resolve the issue efficiently. Secondly, 
it fosters improved communication by offering a platform for respectful interaction between parties involved. 

**Step-1:-** We need to register in this website and give all the neccessary details which helps the user to communicate us. We also need to choose the contact method. These deatils will saved in our database which helps futher to contact us.

![image](https://github.com/sridharindraganti/Networking-Social/assets/112465823/35700b55-93e0-4265-a4f9-cc142578c860)

**Step-2:-** Using this search page we can scan the vehicle number and search for the details.

![image](https://github.com/sridharindraganti/Networking-Social/assets/112465823/93239f90-e55a-4222-885f-c7a3bb3b3ac6)

**Step-3:-** If the details of that vehicle owner are stored in our database then the details are displayed same like in the below image.

![image](https://github.com/sridharindraganti/Networking-Social/assets/112465823/47e67e28-2376-4cc7-bcc9-cc047f341fd4)

**Step-4:-** After clicking on the contact method button then some predefiened messages are displayed like in the below image. We need to select the message which we want to send to the owner.

![image](https://github.com/sridharindraganti/Networking-Social/assets/112465823/0828dc5e-afbb-4cd9-9a3e-998734131754)




