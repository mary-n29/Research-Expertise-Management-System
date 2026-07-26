CREATE DATABASE ResearchExpertiseDB;
USE ResearchExpertiseDB;

CREATE TABLE SPONSOR (
    SponsorID INT PRIMARY KEY,
    SName VARCHAR(100) NOT NULL,
    SType VARCHAR(50) NOT NULL,
    POCFName VARCHAR(50) NOT NULL,
    POCLName VARCHAR(50) NOT NULL,
    POCEmail VARCHAR(100) NOT NULL UNIQUE
);

-- ============================================================
-- PROJECT
-- ============================================================

CREATE TABLE PROJECT (
    ProjectID INT PRIMARY KEY,
    PName VARCHAR(150) NOT NULL,
    PDescription VARCHAR(500),
    FundingAmount DECIMAL(12,2) NOT NULL,
    Status VARCHAR(50) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    SponsorID INT NOT NULL,

    CONSTRAINT chk_project_funding
        CHECK (FundingAmount >= 0),

    CONSTRAINT chk_project_dates
        CHECK (EndDate IS NULL OR EndDate >= StartDate),

    CONSTRAINT fk_project_sponsor
        FOREIGN KEY (SponsorID)
        REFERENCES SPONSOR(SponsorID)
);


-- ============================================================
-- DELIVERABLE
-- ============================================================

CREATE TABLE DELIVERABLE (
    DeliverableID INT PRIMARY KEY,
    DTitle VARCHAR(150) NOT NULL,
    DelStatus VARCHAR(20) NOT NULL,
    DueDate DATE NOT NULL,
    SubDate DATE,
    ProjectID INT NOT NULL,

    CONSTRAINT chk_deliverable_status
        CHECK (
            DelStatus IN (
                'Pending',
                'Submitted',
                'Approved',
                'Rejected'
            )
        ),

    CONSTRAINT fk_deliverable_project
        FOREIGN KEY (ProjectID)
        REFERENCES PROJECT(ProjectID)
);


-- ============================================================
-- RESEARCHER
-- ============================================================

CREATE TABLE RESEARCHER (
    ResearcherID INT PRIMARY KEY,
    FName VARCHAR(50) NOT NULL,
    LName VARCHAR(50) NOT NULL,
    Department VARCHAR(100) NOT NULL,
    Position VARCHAR(100) NOT NULL
);


-- ============================================================
-- PROJECT_MEMBERSHIP
-- ============================================================

CREATE TABLE PROJECT_MEMBERSHIP (
    ProjectID INT NOT NULL,
    ResearcherID INT NOT NULL,
    JoinDate DATE NOT NULL,

    CONSTRAINT pk_project_membership
        PRIMARY KEY (ProjectID, ResearcherID),

    CONSTRAINT fk_membership_project
        FOREIGN KEY (ProjectID)
        REFERENCES PROJECT(ProjectID),

    CONSTRAINT fk_membership_researcher
        FOREIGN KEY (ResearcherID)
        REFERENCES RESEARCHER(ResearcherID)
);


-- ============================================================
-- SKILL
-- ============================================================

CREATE TABLE SKILL (
    SkillID INT PRIMARY KEY,
    SkillName VARCHAR(100) NOT NULL UNIQUE
);


-- ============================================================
-- RESEARCHER_SKILL
-- ============================================================

CREATE TABLE RESEARCHER_SKILL (
    ResearcherID INT NOT NULL,
    SkillID INT NOT NULL,
    ProficiencyLevel VARCHAR(20) NOT NULL,

    CONSTRAINT pk_researcher_skill
        PRIMARY KEY (ResearcherID, SkillID),

    CONSTRAINT chk_proficiency_level
        CHECK (
            ProficiencyLevel IN (
                'Beginner',
                'Intermediate',
                'Advanced',
                'Expert'
            )
        ),

    CONSTRAINT fk_rs_researcher
        FOREIGN KEY (ResearcherID)
        REFERENCES RESEARCHER(ResearcherID),

    CONSTRAINT fk_rs_skill
        FOREIGN KEY (SkillID)
        REFERENCES SKILL(SkillID)
);


-- ============================================================
-- PUBLICATION
-- ============================================================

CREATE TABLE PUBLICATION (
    PublicationID INT PRIMARY KEY,
    PubTitle VARCHAR(250) NOT NULL,
    PubDate DATE,
    DOI VARCHAR(255) UNIQUE
);


-- ============================================================
-- PUBLICATION_AUTHOR
-- ============================================================

CREATE TABLE PUBLICATION_AUTHOR (
    PublicationID INT NOT NULL,
    ResearcherID INT NOT NULL,

    CONSTRAINT pk_publication_author
        PRIMARY KEY (PublicationID, ResearcherID),

    CONSTRAINT fk_pa_publication
        FOREIGN KEY (PublicationID)
        REFERENCES PUBLICATION(PublicationID),

    CONSTRAINT fk_pa_researcher
        FOREIGN KEY (ResearcherID)
        REFERENCES RESEARCHER(ResearcherID)
);


-- ============================================================
-- RESEARCH_AREA
-- ============================================================

CREATE TABLE RESEARCH_AREA (
    ResearchAreaID INT PRIMARY KEY,
    RAreaName VARCHAR(100) NOT NULL UNIQUE,
    RAreaDescription VARCHAR(500)
);
