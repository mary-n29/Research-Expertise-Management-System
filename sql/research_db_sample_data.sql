USE ResearchExpertiseDB;

-- ============================================================
-- 1. SPONSOR - 30 rows
-- ============================================================

INSERT INTO SPONSOR
(SponsorID, SName, SType, POCFName, POCLName, POCEmail)
VALUES
(1, 'National Science Foundation', 'Federal Agency', 'Emma', 'Carter', 'emma.carter@example.org'),
(2, 'National Institutes of Health', 'Federal Agency', 'Liam', 'Brooks', 'liam.brooks@example.org'),
(3, 'Advanced Computing Research Foundation', 'Research Foundation', 'Olivia', 'Reed', 'olivia.reed@example.org'),
(4, 'Horizon Biomedical Research Institute', 'Research Institute', 'Noah', 'Foster', 'noah.foster@example.org'),
(5, 'Center for Autonomous Systems Research', 'Research Center', 'Ava', 'Morgan', 'ava.morgan@example.org'),
(6, 'Digital Security Research Foundation', 'Research Foundation', 'Ethan', 'Ward', 'ethan.ward@example.org'),
(7, 'Future Energy Research Council', 'Research Council', 'Sophia', 'Turner', 'sophia.turner@example.org'),
(8, 'Quantum Technology Initiative', 'Research Initiative', 'Lucas', 'Bennett', 'lucas.bennett@example.org'),
(9, 'Global Data Science Foundation', 'Research Foundation', 'Mia', 'Parker', 'mia.parker@example.org'),
(10, 'Intelligent Robotics Institute', 'Research Institute', 'James', 'Collins', 'james.collins@example.org'),
(11, 'Computational Health Foundation', 'Research Foundation', 'Amelia', 'Hughes', 'amelia.hughes@example.org'),
(12, 'Advanced Materials Research Council', 'Research Council', 'Benjamin', 'Price', 'benjamin.price@example.org'),
(13, 'Sustainable Technology Foundation', 'Research Foundation', 'Charlotte', 'Gray', 'charlotte.gray@example.org'),
(14, 'Cloud Systems Research Alliance', 'Research Alliance', 'Henry', 'Ross', 'henry.ross@example.org'),
(15, 'Human Centered Computing Institute', 'Research Institute', 'Harper', 'Bell', 'harper.bell@example.org'),
(16, 'Secure Infrastructure Research Center', 'Research Center', 'Alexander', 'Cook', 'alexander.cook@example.org'),
(17, 'Applied AI Research Foundation', 'Research Foundation', 'Evelyn', 'Bailey', 'evelyn.bailey@example.org'),
(18, 'Environmental Computing Initiative', 'Research Initiative', 'Daniel', 'Rivera', 'daniel.rivera@example.org'),
(19, 'Smart Cities Research Council', 'Research Council', 'Abigail', 'Cooper', 'abigail.cooper@example.org'),
(20, 'Advanced Networking Institute', 'Research Institute', 'Matthew', 'Richardson', 'matthew.richardson@example.org'),
(21, 'Bioinformatics Research Alliance', 'Research Alliance', 'Ella', 'Cox', 'ella.cox@example.org'),
(22, 'Scientific Software Foundation', 'Research Foundation', 'Jackson', 'Howard', 'jackson.howard@example.org'),
(23, 'Digital Learning Research Center', 'Research Center', 'Scarlett', 'Wood', 'scarlett.wood@example.org'),
(24, 'Next Generation Systems Institute', 'Research Institute', 'Sebastian', 'Watson', 'sebastian.watson@example.org'),
(25, 'Computational Science Research Council', 'Research Council', 'Grace', 'Murphy', 'grace.murphy@example.org'),
(26, 'Emerging Technology Foundation', 'Research Foundation', 'David', 'Peterson', 'david.peterson@example.org'),
(27, 'Advanced Sensor Research Institute', 'Research Institute', 'Chloe', 'Sanders', 'chloe.sanders@example.org'),
(28, 'Resilient Systems Research Center', 'Research Center', 'Joseph', 'Bryant', 'joseph.bryant@example.org'),
(29, 'Health Data Innovation Foundation', 'Research Foundation', 'Victoria', 'Russell', 'victoria.russell@example.org'),
(30, 'Future Computing Research Alliance', 'Research Alliance', 'Samuel', 'Griffin', 'samuel.griffin@example.org');


-- ============================================================
-- 2. RESEARCHER - 30 rows
-- ============================================================

INSERT INTO RESEARCHER
(ResearcherID, FName, LName, Department, Position)
VALUES
(1, 'Olivia', 'Bennett', 'Computer Science', 'Professor'),
(2, 'Ethan', 'Collins', 'Computer Science', 'Associate Professor'),
(3, 'Sophia', 'Ramirez', 'Biomedical Engineering', 'Assistant Professor'),
(4, 'Liam', 'Parker', 'Electrical Engineering', 'Professor'),
(5, 'Ava', 'Thompson', 'Data Science', 'Research Scientist'),
(6, 'Noah', 'Hughes', 'Mechanical Engineering', 'Associate Professor'),
(7, 'Mia', 'Foster', 'Cybersecurity', 'Research Scientist'),
(8, 'Lucas', 'Morgan', 'Computer Science', 'Assistant Professor'),
(9, 'Isabella', 'Ward', 'Biomedical Engineering', 'Research Scientist'),
(10, 'James', 'Cooper', 'Electrical Engineering', 'Professor'),
(11, 'Amelia', 'Reed', 'Data Science', 'Assistant Professor'),
(12, 'Benjamin', 'Turner', 'Computer Science', 'Research Scientist'),
(13, 'Charlotte', 'Bailey', 'Mechanical Engineering', 'Professor'),
(14, 'Henry', 'Richardson', 'Cybersecurity', 'Associate Professor'),
(15, 'Harper', 'Cox', 'Information Technology', 'Research Scientist'),
(16, 'Alexander', 'Howard', 'Computer Science', 'Professor'),
(17, 'Evelyn', 'Peterson', 'Biomedical Engineering', 'Associate Professor'),
(18, 'Daniel', 'Gray', 'Electrical Engineering', 'Research Scientist'),
(19, 'Abigail', 'Ross', 'Data Science', 'Professor'),
(20, 'Matthew', 'Murphy', 'Computer Science', 'Assistant Professor'),
(21, 'Ella', 'Rivera', 'Bioinformatics', 'Research Scientist'),
(22, 'Jackson', 'Bell', 'Computer Science', 'Associate Professor'),
(23, 'Scarlett', 'Cook', 'Information Technology', 'Assistant Professor'),
(24, 'Sebastian', 'Price', 'Mechanical Engineering', 'Research Scientist'),
(25, 'Grace', 'Watson', 'Data Science', 'Associate Professor'),
(26, 'David', 'Sanders', 'Cybersecurity', 'Professor'),
(27, 'Chloe', 'Bryant', 'Biomedical Engineering', 'Research Scientist'),
(28, 'Joseph', 'Russell', 'Electrical Engineering', 'Associate Professor'),
(29, 'Victoria', 'Griffin', 'Bioinformatics', 'Assistant Professor'),
(30, 'Samuel', 'Hayes', 'Computer Science', 'Research Scientist');


-- ============================================================
-- 3. SKILL - 30 rows
-- ============================================================

INSERT INTO SKILL
(SkillID, SkillName)
VALUES
(1, 'Machine Learning'),
(2, 'Data Analysis'),
(3, 'Python Programming'),
(4, 'Cybersecurity'),
(5, 'Computer Vision'),
(6, 'Robotics'),
(7, 'Cloud Computing'),
(8, 'Natural Language Processing'),
(9, 'Statistical Modeling'),
(10, 'Database Systems'),
(11, 'Deep Learning'),
(12, 'Bioinformatics'),
(13, 'Data Visualization'),
(14, 'High Performance Computing'),
(15, 'Network Security'),
(16, 'Software Engineering'),
(17, 'Artificial Intelligence'),
(18, 'Signal Processing'),
(19, 'Embedded Systems'),
(20, 'Scientific Computing'),
(21, 'Big Data Analytics'),
(22, 'Distributed Systems'),
(23, 'Reinforcement Learning'),
(24, 'Image Processing'),
(25, 'Optimization'),
(26, 'Cloud Security'),
(27, 'Research Data Management'),
(28, 'Predictive Modeling'),
(29, 'Web Development'),
(30, 'Data Mining');


-- ============================================================
-- 4. RESEARCH_AREA - 30 rows
-- ============================================================

INSERT INTO RESEARCH_AREA
(ResearchAreaID, RAreaName, RAreaDescription)
VALUES
(1, 'Artificial Intelligence', 'Research on intelligent computational systems.'),
(2, 'Cybersecurity', 'Security and protection of computational systems and information.'),
(3, 'Biomedical Informatics', 'Computational analysis of biomedical and health information.'),
(4, 'Robotics', 'Design and development of robotic systems.'),
(5, 'Data Science', 'Methods for extracting knowledge and insights from data.'),
(6, 'Computer Vision', 'Computational interpretation of images and video.'),
(7, 'High Performance Computing', 'Large-scale and high-performance computational systems.'),
(8, 'Energy Systems', 'Computational approaches to energy production and optimization.'),
(9, 'Machine Learning', 'Algorithms capable of learning patterns from data.'),
(10, 'Autonomous Systems', 'Systems capable of independent sensing and decision making.'),
(11, 'Natural Language Processing', 'Computational processing of human language.'),
(12, 'Bioinformatics', 'Computational analysis of biological information.'),
(13, 'Cloud Computing', 'Scalable computing resources and services delivered through networks.'),
(14, 'Database Systems', 'Storage, organization, retrieval, and management of structured data.'),
(15, 'Human Computer Interaction', 'Research on interaction between people and computing systems.'),
(16, 'Quantum Computing', 'Computational techniques based on quantum information principles.'),
(17, 'Scientific Computing', 'Computational methods for scientific problems.'),
(18, 'Computer Networks', 'Communication protocols and interconnected computing systems.'),
(19, 'Software Engineering', 'Methods for designing and maintaining software systems.'),
(20, 'Information Retrieval', 'Methods for finding relevant information in large collections.'),
(21, 'Distributed Systems', 'Computing systems operating across multiple connected machines.'),
(22, 'Health Data Analytics', 'Analysis of health and clinical datasets.'),
(23, 'Smart Cities', 'Computing technologies supporting intelligent urban environments.'),
(24, 'Internet of Things', 'Networks of connected sensing and computing devices.'),
(25, 'Privacy Engineering', 'Design of systems that protect personal and sensitive information.'),
(26, 'Computational Biology', 'Computational modeling and analysis of biological processes.'),
(27, 'Data Mining', 'Discovery of useful patterns in large datasets.'),
(28, 'Embedded Systems', 'Computing systems integrated into specialized hardware.'),
(29, 'Signal Processing', 'Analysis and transformation of digital and analog signals.'),
(30, 'Computational Sustainability', 'Computational approaches to environmental and sustainability challenges.');


-- ============================================================
-- 5. PROJECT - 30 rows
-- Each SponsorID references an existing SPONSOR
-- ============================================================

INSERT INTO PROJECT
(ProjectID, PName, PDescription, FundingAmount, Status,
 StartDate, EndDate, SponsorID)
VALUES
(1, 'AI for Scientific Discovery', 'AI methods for scientific data analysis.', 850000.00, 'Active', '2025-01-15', '2027-12-31', 1),
(2, 'Biomedical Imaging Analytics', 'Machine learning for biomedical imaging analysis.', 1200000.00, 'Active', '2025-03-01', '2028-02-28', 2),
(3, 'Autonomous Cyber Defense', 'Automated detection and response to cyber threats.', 2100000.00, 'Active', '2024-09-01', '2027-08-31', 3),
(4, 'Maritime Sensor Intelligence', 'Intelligent analysis of distributed sensor information.', 975000.00, 'Active', '2025-06-01', '2027-05-31', 4),
(5, 'Energy Efficient Computing', 'Reducing energy consumption in large computing systems.', 1400000.00, 'Active', '2025-02-01', '2028-01-31', 5),
(6, 'Trustworthy Machine Learning', 'Improving reliability and explainability of machine learning.', 725000.00, 'Active', '2025-09-01', '2027-08-31', 6),
(7, 'Computational Health Modeling', 'Computational models for complex health datasets.', 1100000.00, 'Active', '2024-08-15', '2027-08-14', 7),
(8, 'Resilient Autonomous Systems', 'Autonomous systems operating under uncertain conditions.', 1850000.00, 'Active', '2025-01-01', '2027-12-31', 8),
(9, 'Advanced Robotics Platform', 'Intelligent robotic technologies for challenging environments.', 1600000.00, 'Active', '2025-04-01', '2028-03-31', 9),
(10, 'Smart Energy Data Systems', 'Data-driven monitoring and optimization of energy systems.', 950000.00, 'Active', '2025-10-01', '2028-09-30', 10),
(11, 'Language Intelligence Platform', 'Natural language processing for scientific documents.', 680000.00, 'Active', '2025-05-01', '2027-04-30', 11),
(12, 'Genomic Data Analytics', 'Scalable methods for analyzing genomic datasets.', 1350000.00, 'Active', '2024-10-01', '2027-09-30', 12),
(13, 'Sustainable Computing Infrastructure', 'Energy-conscious computing infrastructure research.', 890000.00, 'Active', '2025-07-01', '2027-06-30', 13),
(14, 'Secure Cloud Research', 'Security techniques for distributed cloud environments.', 1150000.00, 'Active', '2025-02-15', '2028-02-14', 14),
(15, 'Accessible Human AI Interaction', 'Human-centered interfaces for AI systems.', 640000.00, 'Active', '2025-08-01', '2027-07-31', 15),
(16, 'Resilient Digital Infrastructure', 'Methods for improving infrastructure resilience.', 1725000.00, 'Active', '2024-11-01', '2027-10-31', 16),
(17, 'Applied AI Decision Support', 'AI tools supporting complex decision-making tasks.', 810000.00, 'Active', '2025-01-10', '2027-01-09', 17),
(18, 'Environmental Data Intelligence', 'Computational analysis of environmental datasets.', 760000.00, 'Active', '2025-03-15', '2027-03-14', 18),
(19, 'Urban Mobility Analytics', 'Data analytics for intelligent urban transportation.', 920000.00, 'Active', '2025-06-15', '2028-06-14', 19),
(20, 'Next Generation Networking', 'Research on scalable and resilient network architectures.', 1300000.00, 'Active', '2024-12-01', '2027-11-30', 20),
(21, 'Precision Bioinformatics', 'Bioinformatics methods for precision health research.', 1450000.00, 'Active', '2025-04-15', '2028-04-14', 21),
(22, 'Scientific Software Reliability', 'Techniques for reliable scientific software.', 590000.00, 'Active', '2025-09-01', '2027-08-31', 22),
(23, 'Adaptive Digital Learning', 'Data-driven adaptive learning technologies.', 540000.00, 'Active', '2025-05-20', '2027-05-19', 23),
(24, 'Intelligent Distributed Systems', 'AI-enabled distributed computing architectures.', 1250000.00, 'Active', '2025-02-01', '2028-01-31', 24),
(25, 'Scalable Scientific Analytics', 'High-performance analytics for scientific datasets.', 980000.00, 'Active', '2025-07-15', '2027-07-14', 25),
(26, 'Emerging Computing Technologies', 'Evaluation of emerging computational technologies.', 1050000.00, 'Active', '2025-01-20', '2028-01-19', 26),
(27, 'Intelligent Sensor Networks', 'AI-enabled distributed sensor networks.', 870000.00, 'Active', '2025-04-01', '2027-03-31', 27),
(28, 'Resilient Computing Systems', 'Design of dependable and resilient computing systems.', 1180000.00, 'Active', '2024-09-15', '2027-09-14', 28),
(29, 'Health Data Integration', 'Secure integration and analysis of health datasets.', 1320000.00, 'Active', '2025-03-01', '2028-02-29', 29),
(30, 'Future Computing Architecture', 'Research on next-generation computing architectures.', 1550000.00, 'Active', '2025-06-01', '2028-05-31', 30);


-- ============================================================
-- 6. DELIVERABLE - 35 rows
-- ============================================================

INSERT INTO DELIVERABLE
(DeliverableID, DTitle, DelStatus, DueDate, SubDate, ProjectID)
VALUES
(1, 'AI Research Plan', 'Approved', '2025-03-01', '2025-02-25', 1),
(2, 'Imaging Dataset Report', 'Approved', '2025-06-01', '2025-05-28', 2),
(3, 'Cyber Defense Prototype', 'Approved', '2025-04-15', '2025-04-10', 3),
(4, 'Sensor Architecture Report', 'Submitted', '2026-08-01', '2026-07-28', 4),
(5, 'Energy Benchmark Report', 'Approved', '2025-12-01', '2025-11-27', 5),
(6, 'Trustworthy AI Framework', 'Submitted', '2026-06-01', '2026-05-29', 6),
(7, 'Health Modeling Prototype', 'Approved', '2025-08-15', '2025-08-11', 7),
(8, 'Autonomous Systems Test Plan', 'Submitted', '2026-05-15', '2026-05-12', 8),
(9, 'Robotics Prototype', 'Approved', '2026-01-20', '2026-01-17', 9),
(10, 'Energy Data Architecture', 'Submitted', '2026-04-15', '2026-04-12', 10),
(11, 'NLP Evaluation Report', 'Approved', '2025-11-01', '2025-10-28', 11),
(12, 'Genomics Pipeline', 'Submitted', '2026-02-01', '2026-01-29', 12),
(13, 'Sustainability Assessment', 'Approved', '2026-01-15', '2026-01-12', 13),
(14, 'Cloud Security Prototype', 'Submitted', '2026-03-15', '2026-03-11', 14),
(15, 'User Interaction Study', 'Approved', '2026-02-15', '2026-02-12', 15),
(16, 'Infrastructure Risk Report', 'Approved', '2025-10-15', '2025-10-11', 16),
(17, 'Decision Support Prototype', 'Submitted', '2026-01-10', '2026-01-08', 17),
(18, 'Environmental Dataset', 'Approved', '2025-12-15', '2025-12-10', 18),
(19, 'Mobility Analytics Dashboard', 'Submitted', '2026-06-15', '2026-06-12', 19),
(20, 'Network Architecture Prototype', 'Approved', '2025-09-01', '2025-08-29', 20),
(21, 'Bioinformatics Analysis Report', 'Submitted', '2026-05-01', '2026-04-27', 21),
(22, 'Software Reliability Report', 'Approved', '2026-03-01', '2026-02-25', 22),
(23, 'Adaptive Learning Prototype', 'Submitted', '2026-02-20', '2026-02-18', 23),
(24, 'Distributed Systems Benchmark', 'Approved', '2025-12-01', '2025-11-26', 24),
(25, 'Scientific Analytics Prototype', 'Submitted', '2026-04-01', '2026-03-29', 25),
(26, 'Technology Evaluation Report', 'Approved', '2025-11-20', '2025-11-17', 26),
(27, 'Sensor Network Prototype', 'Submitted', '2026-01-15', '2026-01-11', 27),
(28, 'Resilience Testing Report', 'Approved', '2025-08-15', '2025-08-12', 28),
(29, 'Health Integration Prototype', 'Submitted', '2026-03-01', '2026-02-27', 29),
(30, 'Architecture Design Report', 'Approved', '2026-02-01', '2026-01-28', 30),
(31, 'AI Model Evaluation', 'Pending', '2027-01-15', NULL, 1),
(32, 'Biomedical Validation Report', 'Pending', '2027-03-01', NULL, 2),
(33, 'Cybersecurity Final Evaluation', 'Pending', '2027-02-15', NULL, 3),
(34, 'Cloud Security Final Report', 'Pending', '2027-06-15', NULL, 14),
(35, 'Health Data Final Report', 'Pending', '2027-08-01', NULL, 29);


-- ============================================================
-- 7. PUBLICATION - 30 rows
-- All publications and DOI-style values are synthetic.
-- ============================================================

INSERT INTO PUBLICATION
(PublicationID, PubTitle, PubDate, DOI)
VALUES
(1, 'Explainable Models for Scientific Data Analysis', '2025-02-10', '10.9999/demo001'),
(2, 'Deep Learning Methods for Biomedical Imaging', '2025-04-18', '10.9999/demo002'),
(3, 'Adaptive Detection of Emerging Cyber Threats', '2025-01-05', '10.9999/demo003'),
(4, 'Distributed Intelligence for Sensor Networks', '2025-07-22', '10.9999/demo004'),
(5, 'Energy Aware High Performance Computing', '2025-05-12', '10.9999/demo005'),
(6, 'Reliable Machine Learning Under Distribution Shift', '2025-09-08', '10.9999/demo006'),
(7, 'Predictive Modeling for Complex Health Data', '2025-09-14', '10.9999/demo007'),
(8, 'Resilient Decision Making for Autonomous Systems', '2025-10-20', '10.9999/demo008'),
(9, 'Intelligent Navigation for Robotic Platforms', '2026-01-17', '10.9999/demo009'),
(10, 'Data Driven Optimization of Smart Energy Systems', '2026-04-11', '10.9999/demo010'),
(11, 'Language Models for Scientific Information Extraction', '2025-08-05', '10.9999/demo011'),
(12, 'Scalable Analysis of Genomic Data', '2025-06-13', '10.9999/demo012'),
(13, 'Sustainable Design for Computing Infrastructure', '2025-11-21', '10.9999/demo013'),
(14, 'Security Models for Distributed Cloud Systems', '2026-02-14', '10.9999/demo014'),
(15, 'Human Centered Evaluation of Intelligent Interfaces', '2025-12-07', '10.9999/demo015'),
(16, 'Resilience Metrics for Digital Infrastructure', '2025-03-19', '10.9999/demo016'),
(17, 'Artificial Intelligence for Decision Support', '2025-07-08', '10.9999/demo017'),
(18, 'Machine Learning for Environmental Data', '2025-10-11', '10.9999/demo018'),
(19, 'Urban Mobility Prediction Using Large Scale Data', '2026-01-23', '10.9999/demo019'),
(20, 'Resilient Architectures for Future Networks', '2025-05-29', '10.9999/demo020'),
(21, 'Computational Methods for Precision Bioinformatics', '2026-03-12', '10.9999/demo021'),
(22, 'Improving Reliability in Scientific Software', '2025-09-26', '10.9999/demo022'),
(23, 'Adaptive Models for Digital Learning Environments', '2026-02-08', '10.9999/demo023'),
(24, 'Intelligent Resource Allocation in Distributed Systems', '2025-11-14', '10.9999/demo024'),
(25, 'Scalable Analytics for Scientific Workloads', '2026-04-02', '10.9999/demo025'),
(26, 'Evaluation Methods for Emerging Computing Systems', '2025-08-18', '10.9999/demo026'),
(27, 'Machine Intelligence for Distributed Sensors', '2026-01-09', '10.9999/demo027'),
(28, 'Dependability Models for Resilient Computing', '2025-06-24', '10.9999/demo028'),
(29, 'Secure Integration of Heterogeneous Health Data', '2026-03-28', '10.9999/demo029'),
(30, 'Architectures for Next Generation Computing', '2026-05-16', '10.9999/demo030');


-- ============================================================
-- 8. PROJECT_MEMBERSHIP - 60 rows
-- Each project gets two researchers.
-- ============================================================

INSERT INTO PROJECT_MEMBERSHIP
(ProjectID, ResearcherID, JoinDate)
VALUES
(1,1,'2025-01-15'), (1,5,'2025-02-01'),
(2,3,'2025-03-01'), (2,9,'2025-03-10'),
(3,7,'2024-09-01'), (3,14,'2024-09-15'),
(4,4,'2025-06-01'), (4,18,'2025-06-10'),
(5,6,'2025-02-01'), (5,19,'2025-02-15'),
(6,1,'2025-09-01'), (6,8,'2025-09-10'),
(7,3,'2024-08-15'), (7,21,'2024-09-01'),
(8,6,'2025-01-01'), (8,24,'2025-01-15'),
(9,10,'2025-04-01'), (9,13,'2025-04-10'),
(10,5,'2025-10-01'), (10,25,'2025-10-15'),
(11,8,'2025-05-01'), (11,22,'2025-05-15'),
(12,12,'2024-10-01'), (12,29,'2024-10-15'),
(13,14,'2025-07-01'), (13,19,'2025-07-10'),
(14,7,'2025-02-15'), (14,26,'2025-03-01'),
(15,15,'2025-08-01'), (15,20,'2025-08-15'),
(16,2,'2024-11-01'), (16,26,'2024-11-15'),
(17,1,'2025-01-10'), (17,11,'2025-01-20'),
(18,11,'2025-03-15'), (18,25,'2025-04-01'),
(19,19,'2025-06-15'), (19,23,'2025-07-01'),
(20,2,'2024-12-01'), (20,28,'2024-12-15'),
(21,17,'2025-04-15'), (21,29,'2025-05-01'),
(22,16,'2025-09-01'), (22,30,'2025-09-15'),
(23,20,'2025-05-20'), (23,23,'2025-06-01'),
(24,12,'2025-02-01'), (24,22,'2025-02-15'),
(25,16,'2025-07-15'), (25,25,'2025-08-01'),
(26,18,'2025-01-20'), (26,30,'2025-02-01'),
(27,10,'2025-04-01'), (27,28,'2025-04-15'),
(28,14,'2024-09-15'), (28,26,'2024-10-01'),
(29,17,'2025-03-01'), (29,27,'2025-03-15'),
(30,4,'2025-06-01'), (30,24,'2025-06-15');


-- ============================================================
-- 9. RESEARCHER_SKILL - 75 rows
-- ============================================================

INSERT INTO RESEARCHER_SKILL
(ResearcherID, SkillID, ProficiencyLevel)
VALUES
(1,1,'Expert'), (1,3,'Expert'), (1,17,'Advanced'),
(2,4,'Advanced'), (2,15,'Expert'), (2,16,'Advanced'),
(3,5,'Expert'), (3,9,'Advanced'), (3,24,'Advanced'),
(4,18,'Expert'), (4,19,'Advanced'), (4,6,'Intermediate'),
(5,2,'Expert'), (5,13,'Advanced'), (5,21,'Expert'),
(6,6,'Expert'), (6,25,'Advanced'),
(7,4,'Expert'), (7,15,'Expert'), (7,26,'Advanced'),
(8,1,'Advanced'), (8,8,'Expert'), (8,3,'Advanced'),
(9,5,'Advanced'), (9,12,'Expert'),
(10,6,'Expert'), (10,18,'Advanced'), (10,19,'Advanced'),
(11,2,'Expert'), (11,9,'Expert'), (11,28,'Advanced'),
(12,3,'Expert'), (12,14,'Advanced'),
(13,6,'Advanced'), (13,19,'Expert'),
(14,4,'Expert'), (14,15,'Expert'), (14,26,'Expert'),
(15,7,'Advanced'), (15,10,'Advanced'),
(16,16,'Expert'), (16,20,'Advanced'), (16,3,'Advanced'),
(17,12,'Expert'), (17,9,'Advanced'),
(18,18,'Expert'), (18,20,'Advanced'),
(19,2,'Expert'), (19,21,'Expert'), (19,13,'Advanced'),
(20,16,'Advanced'), (20,29,'Expert'),
(21,12,'Expert'), (21,30,'Advanced'), (21,3,'Advanced'),
(22,16,'Expert'), (22,22,'Advanced'),
(23,7,'Advanced'), (23,29,'Expert'),
(24,6,'Expert'), (24,25,'Advanced'),
(25,2,'Expert'), (25,9,'Advanced'), (25,28,'Expert'),
(26,4,'Expert'), (26,15,'Expert'),
(27,5,'Expert'), (27,12,'Advanced'),
(28,18,'Expert'), (28,19,'Advanced'),
(29,12,'Expert'), (29,30,'Advanced'), (29,2,'Advanced'),
(30,3,'Expert'), (30,10,'Expert'), (30,16,'Advanced');


-- ============================================================
-- 10. PUBLICATION_AUTHOR - 45 rows
-- ============================================================

INSERT INTO PUBLICATION_AUTHOR
(PublicationID, ResearcherID)
VALUES
(1,1), (1,5),
(2,3), (2,9),
(3,7), (3,14),
(4,4), (4,18),
(5,6), (5,19),
(6,1), (6,8),
(7,3), (7,21),
(8,6), (8,24),
(9,10), (9,13),
(10,5), (10,25),
(11,8), (11,22),
(12,12), (12,29),
(13,19),
(14,7), (14,26),
(15,15), (15,20),
(16,26),
(17,1), (17,11),
(18,25),
(19,19), (19,23),
(20,2), (20,28),
(21,17), (21,29),
(22,16),
(23,20),
(24,12), (24,22),
(25,25),
(26,30),
(27,10), (27,28),
(28,14),
(29,17), (29,27),
(30,4), (30,24);