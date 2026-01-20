# GreenPower Solutions - Technical Documentation
## Comprehensive Guide to Autonomous Solar Generation Systems

**Version:** 3.1  
**Last Updated:** January 2025  
**Document ID:** GP-TECH-DOC-2025-001  
**Classification:** Public - Technical Reference

---

## Table of Contents

1. [Company Overview](#company-overview)
2. [Technology Foundation](#technology-foundation)
3. [Product Line Specifications](#product-line-specifications)
4. [Installation Guidelines](#installation-guidelines)
5. [Operation & Maintenance](#operation-maintenance)
6. [Troubleshooting Guide](#troubleshooting-guide)
7. [Safety & Compliance](#safety-compliance)
8. [Performance Optimization](#performance-optimization)
9. [Technical Support](#technical-support)
10. [Appendices](#appendices)

---

## 1. Company Overview

### About GreenPower Solutions

**Founded:** 2011  
**Headquarters:** Perpignan, Pyrénées-Orientales, France  
**Founder & CEO:** Vincent Theroux  
**Core Mission:** Provide autonomous, emission-free electrical power generation systems using solar energy and advanced battery storage technology.

### Our Innovation

GreenPower Solutions pioneered the integration of second-life electric vehicle batteries with high-efficiency solar panels to create truly autonomous mobile power systems. Our technology eliminates the need for diesel generators while providing 24/7/365 reliable electricity.

### Certifications & Standards

- **CE Certification:** All products (Full compliance)
- **DIN VDE 0126-1-1:** Grid connection and safety standards
- **NF C15-100-712:** French electrical installation standards (Sections 1, 2, 3)
- **CONSUEL Approved:** French electrical safety committee certification
- **ISO 9001:2015:** Quality management systems
- **ISO 14001:2015:** Environmental management systems

---

## 2. Technology Foundation

### Core Components

#### 2.1 Solar Photovoltaic Panels

**Technology:** Monocrystalline silicon cells  
**Efficiency:** 20-22% conversion rate  
**Warranty:** 25 years (80% output guaranteed)  
**Operating Range:** -40°C to +85°C  
**Certifications:** IEC 61215, IEC 61730

**Panel Specifications by Model:**
- **PG-U01 (Ultra):** 150 kWp total capacity, 300+ panels
- **PG-M01 (Max):** 48 kWp total capacity, 96 panels
- **PG-P01 (Performance):** 24 kWp total capacity, 48 panels
- **PG-C01 (Compact):** 8 kWp total capacity, 16 panels
- **PG-M02 (Mini):** 2 kWp total capacity, 4 portable panels

#### 2.2 Battery Storage Systems

##### Second-Life EV Batteries (PG-U01, PG-M01)
- **Source:** Tesla Model S/X, BMW i3, Nissan Leaf modules
- **Chemistry:** Lithium Nickel Manganese Cobalt Oxide (NMC)
- **Testing:** 100% capacity testing, internal resistance measurement
- **Certification:** European Battery Regulation 2023/1542 compliant
- **Warranty:** 2,000-3,000 cycles or 5-8 years
- **State of Health:** Minimum 75% remaining capacity upon installation

##### LiFePO4 Battery Systems (PG-P01, PG-C01, PG-M02)
- **Chemistry:** Lithium Iron Phosphate (LiFePO4)
- **Advantages:** Longer lifespan, thermal stability, intrinsic safety
- **Cycle Life:** 3,000-5,000 cycles (80% DoD)
- **Operating Temperature:** 0°C to 45°C (with BMS protection)
- **Warranty:** 3,000 cycles or 7-10 years

##### Battery Management System (BMS)
All battery packs include integrated BMS with:
- Individual cell voltage monitoring
- Temperature monitoring (multiple sensors)
- State of Charge (SoC) calculation
- State of Health (SoH) tracking
- Overcurrent/overvoltage/undervoltage protection
- Cell balancing (passive and active)
- Communication interface (CAN bus)

#### 2.3 Power Conversion Equipment

**Manufacturer:** Victron Energy (Netherlands)  
**Technology:** Pure sine wave inverter/chargers  
**Certifications:** CE, DIN VDE, UL (select models)

**Inverter Models by Product:**

| Product | Inverter Model | Continuous Power | Peak Power | Voltage |
|---------|---------------|------------------|------------|---------|
| PG-U01 | Quattro 48/15000 | 15 kVA | 30 kW | 48V DC |
| PG-M01 | Quattro 48/10000 | 10 kVA | 20 kW | 48V DC |
| PG-P01 | MultiPlus-II 48/5000 | 5 kVA | 10 kW | 48V DC |
| PG-C01 | MultiPlus 48/3000 | 3 kVA | 6 kW | 48V DC |
| PG-M02 | Phoenix 48/1200 | 1.2 kVA | 2.4 kW | 48V DC |

**Inverter Features:**
- Pure sine wave output (THD <3%)
- Frequency: 50 Hz ±0.1% (crystal-controlled)
- Voltage regulation: ±2%
- PowerAssist technology (grid or generator support)
- UPS function (20ms switchover)
- Programmable relay outputs

#### 2.4 Solar Charge Controllers

**Technology:** Maximum Power Point Tracking (MPPT)  
**Manufacturer:** Victron Energy SmartSolar series  
**Efficiency:** Up to 98% conversion efficiency

**Features:**
- Advanced MPPT algorithm (updates every 0.5 seconds)
- Cloud detection and response
- Temperature compensation
- Programmable battery charging profiles
- Bluetooth monitoring (VictronConnect app)
- Load output management

---

## 3. Product Line Specifications

### 3.1 PG-U01 (GreenPower Ultra)

**Form Factor:** Standard 20-foot shipping container  
**Dimensions:** 6.0m (L) x 2.5m (W) x 2.8m (H)  
**Weight:** 8,500 kg (fully loaded)  
**Transport:** Flatbed truck, requires crane for loading

**Electrical Specifications:**
- **Nominal Voltage:** 48V DC battery system
- **AC Output:** 400V three-phase, 50 Hz
- **Continuous Power:** 500 kVA (400 kW)
- **Peak Power:** 1,000 kW (2x surge capacity)
- **Battery Capacity:** 2,000 kWh usable
- **Solar Input:** 150 kWp maximum

**Performance Characteristics:**
- **Autonomy:** 4-5 days at 50% load without sun
- **Recharge Time:** 8-10 hours full sun to 100%
- **Efficiency:** 88-92% system (DC to AC)
- **Power Factor:** 0.99 (unity power factor mode)

**Environmental:**
- **Operating Temperature:** -10°C to +45°C
- **Storage Temperature:** -20°C to +60°C
- **Humidity:** 5-95% non-condensing
- **IP Rating:** IP65 (weatherproof, dust-tight)
- **Noise Level:** <45 dB at 1 meter

**Connectivity:**
- **Remote Monitoring:** 4G LTE modem (built-in)
- **Local Control:** 10" color touchscreen
- **Protocols:** Modbus TCP, CAN bus
- **API:** RESTful API for integration

**Applications:**
- Large industrial facilities
- Major festivals (50,000+ attendees)
- Film production studios
- Data centers (backup power)
- Hospital emergency backup
- Military field operations

**Related Documents:**
- `Manual_PG-U01_v4.1.pdf`
- `Installation_Guide_Container_Systems.pdf`
- `PG-U01_Electrical_Schematics.pdf`
- `Remote_Monitoring_Setup_2024.pdf`

---

### 3.2 PG-M01 (GreenPower Max)

**Form Factor:** Enclosed trailer (towable)  
**Dimensions:** 5.0m (L) x 2.0m (W) x 2.5m (H)  
**Weight:** 3,200 kg (GVW: 3,500 kg)  
**Transport:** Towable by pickup truck or van (3.5T license)

**Electrical Specifications:**
- **Nominal Voltage:** 48V DC battery system
- **AC Output:** 400V three-phase OR 230V single-phase
- **Continuous Power:** 180 kVA (144 kW)
- **Peak Power:** 360 kW (2x surge capacity)
- **Battery Capacity:** 720 kWh usable
- **Solar Input:** 48 kWp maximum

**Performance Characteristics:**
- **Autonomy:** 3-4 days at 50% load without sun
- **Recharge Time:** 7-9 hours full sun to 100%
- **Efficiency:** 90-93% system (DC to AC)
- **Power Factor:** 0.98 (adjustable)

**Environmental:**
- **Operating Temperature:** -5°C to +45°C
- **Storage Temperature:** -15°C to +60°C
- **Humidity:** 10-95% non-condensing
- **IP Rating:** IP54 (splash-proof)
- **Noise Level:** <35 dB at 1 meter

**Connectivity:**
- **Remote Monitoring:** 4G LTE + WiFi hotspot
- **Local Control:** 7" touchscreen + physical buttons
- **Protocols:** Modbus RTU/TCP, CAN bus
- **Mobile App:** iOS/Android (GreenPower Connect)

**Applications:**
- Medium-large outdoor events
- Construction sites (ZFE compliance)
- Food trucks and catering
- Agricultural operations
- Film/TV production
- Temporary medical facilities

**Hybrid Mode Capability:**
- Compatible with diesel generators via PG-ACC-03 kit
- Automatic load sharing and switching
- Achieves 95%+ fuel reduction
- Programmable diesel start/stop thresholds

**Related Documents:**
- `Manual_PG-M01_v3.2.pdf`
- `Hybrid_Mode_Configuration_Guide.pdf`
- `Trailer_Towing_Safety_Guidelines.pdf`
- `Case_Study_Festival_Valmanya_2023.pdf`

---

### 3.3 PG-P01 (GreenPower Performance)

**Form Factor:** Compact outdoor cabinet (pallet-mounted)  
**Dimensions:** 3.0m (L) x 1.5m (W) x 2.0m (H)  
**Weight:** 1,400 kg  
**Transport:** Forklift, pallet jack, or small crane

**Electrical Specifications:**
- **Nominal Voltage:** 48V DC battery system
- **AC Output:** 400V three-phase OR 230V single-phase (switchable)
- **Continuous Power:** 80 kVA (64 kW)
- **Peak Power:** 160 kW (2x surge capacity)
- **Battery Capacity:** 320 kWh usable
- **Solar Input:** 24 kWp maximum

**Performance Characteristics:**
- **Autonomy:** 2-3 days at 50% load without sun
- **Recharge Time:** 6-8 hours full sun to 100%
- **Efficiency:** 91-94% system (DC to AC)
- **Expandability:** Modular battery expansion up to 640 kWh

**Environmental:**
- **Operating Temperature:** 0°C to +40°C
- **Storage Temperature:** -10°C to +50°C
- **Humidity:** 10-90% non-condensing
- **IP Rating:** IP44 (splash-proof)
- **Noise Level:** <30 dB at 1 meter

**Connectivity:**
- **Remote Monitoring:** WiFi + Ethernet + optional 4G
- **Local Control:** Web-based dashboard + 5" LCD
- **Protocols:** Modbus TCP, MQTT
- **Integration:** Compatible with building management systems (BMS)

**Special Features:**
- **Grid-Tie Capable:** Can sell excess solar to grid (requires approval)
- **Demand Response:** Programmable load management
- **Time-of-Use Optimization:** Smart charging/discharging

**Applications:**
- Small-medium construction sites
- Outdoor events and concerts
- Agricultural facilities
- Telecom towers
- Camping resorts
- Off-grid homes and buildings

**Related Documents:**
- `Manual_PG-P01_v2.8.pdf`
- `Grid_Tie_Installation_Procedure.pdf`
- `Battery_Expansion_Module_Guide.pdf`
- `BMS_Integration_Technical_Note.pdf`

---

### 3.4 PG-C01 (GreenPower Compact)

**Form Factor:** Wheeled equipment case  
**Dimensions:** 1.8m (L) x 1.0m (W) x 1.5m (H)  
**Weight:** 450 kg  
**Transport:** Wheeled, manually movable, or light vehicle

**Electrical Specifications:**
- **Nominal Voltage:** 48V DC battery system
- **AC Output:** 230V single-phase, 50 Hz
- **Continuous Power:** 24 kVA (19.2 kW)
- **Peak Power:** 48 kW (2x surge capacity)
- **Battery Capacity:** 96 kWh usable
- **Solar Input:** 8 kWp maximum (folding panels)

**Performance Characteristics:**
- **Autonomy:** 1-2 days at 50% load without sun
- **Recharge Time:** 5-7 hours full sun to 100%
- **Efficiency:** 90-92% system (DC to AC)

**Environmental:**
- **Operating Temperature:** 5°C to +40°C
- **Storage Temperature:** -5°C to +45°C
- **Humidity:** 15-90% non-condensing
- **IP Rating:** IP44 (rainproof)
- **Noise Level:** <25 dB at 1 meter

**Connectivity:**
- **Remote Monitoring:** Bluetooth + WiFi
- **Local Control:** LCD display + button interface
- **Mobile App:** GreenPower Connect (simplified interface)

**Unique Features:**
- **Integrated Solar Panels:** Fold-out design (5-minute setup)
- **Built-in LED Work Lights:** 4x 20W LED floodlights
- **USB Charging Ports:** 4x USB-C (65W PD), 2x USB-A
- **True Plug-and-Play:** No installation required

**Applications:**
- Small outdoor events
- Food trucks and mobile vendors
- Emergency response
- Outdoor markets
- Small construction tools
- Off-grid cabins

**Related Documents:**
- `Manual_PG-C01_v1.9.pdf`
- `Quick_Start_Guide_Compact.pdf`
- `Folding_Solar_Panel_Instructions.pdf`
- `Bluetooth_App_User_Manual.pdf`

---

### 3.5 PG-M02 (GreenPower Mini)

**Form Factor:** Portable hard case with handle  
**Dimensions:** 0.8m (L) x 0.6m (W) x 0.7m (H)  
**Weight:** 85 kg  
**Transport:** Hand-carried (two-person lift recommended)

**Electrical Specifications:**
- **Nominal Voltage:** 48V DC battery system
- **AC Output:** 230V single-phase, 50 Hz
- **Continuous Power:** 5 kVA (4 kW)
- **Peak Power:** 10 kW (2x surge capacity)
- **Battery Capacity:** 20 kWh usable
- **Solar Input:** 2 kWp maximum (portable panels)

**Performance Characteristics:**
- **Autonomy:** 8-12 hours at 50% load without sun
- **Recharge Time:** 4-6 hours full sun to 100%
- **Efficiency:** 88-91% system (DC to AC)

**Environmental:**
- **Operating Temperature:** 10°C to +35°C
- **Storage Temperature:** 0°C to +40°C
- **Humidity:** 20-85% non-condensing
- **IP Rating:** IP43 (drip-proof)
- **Noise Level:** <20 dB at 1 meter

**Connectivity:**
- **Remote Monitoring:** Bluetooth only
- **Local Control:** Simple LED indicators + button
- **Mobile App:** GreenPower Connect (basic monitoring)

**Unique Features:**
- **Ultra-Portable:** Single-user deployable
- **Emergency SOS Beacon:** GPS location + distress signal
- **Car Charging:** 12V cigarette lighter input
- **Multiple Outputs:** 2x AC outlets, 4x USB ports, 2x DC outputs

**Applications:**
- Vendor stalls and small businesses
- RV and camper supplemental power
- Emergency home backup
- Disaster relief operations
- Remote scientific equipment
- Outdoor workshops

**Related Documents:**
- `Manual_PG-M02_v1.5.pdf`
- `Portable_Solar_Setup_Guide.pdf`
- `Emergency_Use_Instructions.pdf`
- `Car_Charging_Adapter_Guide.pdf`

---

## 4. Installation Guidelines

### 4.1 Pre-Installation Assessment

**Site Survey Checklist:**
- [ ] Solar exposure analysis (minimum 4 hours direct sun)
- [ ] Ground stability and levelness assessment
- [ ] Access routes for delivery vehicles
- [ ] Environmental hazards (flooding, wind exposure)
- [ ] Distance to loads (cable run calculations)
- [ ] Local regulations and permits
- [ ] Grid connection point (if applicable)

**Tools Required:**
- Multimeter (AC/DC capable)
- Insulation resistance tester (megger)
- Torque wrench (calibrated)
- Cable crimping tools
- Spirit level
- Safety equipment (PPE, lockout/tagout)

### 4.2 Installation Steps (General Procedure)

#### Step 1: Site Preparation
1. Clear and level installation area
2. Verify load-bearing capacity for equipment weight
3. Install drainage if necessary
4. Mark cable routes and connection points

#### Step 2: Equipment Positioning
1. Position GreenPower unit using appropriate lifting equipment
2. Ensure ventilation clearances (minimum 1m on all sides)
3. Level unit within 2° maximum tilt
4. Secure against movement (chocks, anchors, or foundation)

#### Step 3: Solar Panel Deployment
**For Fixed Installations:**
1. Assemble mounting structure per specifications
2. Install panels with proper orientation (South-facing in Northern Hemisphere)
3. Optimize tilt angle for latitude (Perpignan: 38-42° recommended)
4. Secure all connections and hardware to wind rating

**For Mobile Deployments:**
1. Unfold or extend integrated solar arrays
2. Lock panels in position
3. Verify no shading from nearby objects
4. Check panel-to-panel connections

#### Step 4: Electrical Connections
⚠️ **DANGER - Qualified Electrician Required** ⚠️

1. **Verify system is OFF and locked out**
2. Connect solar panel strings to MPPT controllers
   - Verify polarity (DC circuits)
   - Check open-circuit voltage before connection
   - Use proper cable glands and weatherproofing
3. Connect battery system (if modular)
   - Follow color-coded terminal markings
   - Torque bolts to specification (typically 10-15 Nm)
   - Install fuses/breakers as last step
4. Connect inverter to AC distribution
   - Verify phase rotation for three-phase systems
   - Install appropriate overcurrent protection
   - Connect neutral and ground separately
5. Connect loads to system outputs
   - Size cables per NF C15-100 or local codes
   - Label all circuits clearly
   - Install appropriate protection devices

#### Step 5: System Commissioning
1. Perform insulation resistance test (minimum 1 MΩ)
2. Check all terminal torques
3. Power on system in sequence:
   - Battery disconnect
   - Solar charge controllers
   - Inverter/charger
4. Verify voltage and frequency at outputs
5. Perform load test at 25%, 50%, 75%, 100% capacity
6. Configure monitoring and alarms
7. Document all settings and test results

#### Step 6: Training and Handover
1. Operator training (2-4 hours minimum)
2. Demonstrate normal operation procedures
3. Review emergency shutdown procedures
4. Provide documentation package
5. Register system for warranty
6. Schedule first maintenance visit

### 4.3 Installation Times by Model

| Model | Basic Setup | Full Commissioning | Complexity |
|-------|-------------|-------------------|------------|
| PG-U01 | 1-2 days | 2-3 days | High |
| PG-M01 | 4-6 hours | 1 day | Medium |
| PG-P01 | 2-4 hours | 4-6 hours | Medium |
| PG-C01 | 30-60 min | 2-4 hours | Low |
| PG-M02 | 5-15 min | 30-60 min | Very Low |

### 4.4 Special Installation Scenarios

#### Hybrid Diesel Integration
**Required Kit:** PG-ACC-03 Hybrid Diesel Interface Kit

**Installation Steps:**
1. Install hybrid controller module
2. Connect diesel generator to AC coupling point
3. Configure automatic start/stop thresholds
4. Program load sharing priorities
5. Test automatic switchover functionality

**Reference:** `Hybrid_Mode_Configuration_Guide.pdf`

#### Grid-Tie Configuration
**Applicable Models:** PG-P01 and above

**Requirements:**
- Grid-tie inverter module
- Utility approval and interconnection agreement
- Bidirectional meter installation
- Anti-islanding protection

**Reference:** `Grid_Tie_Installation_Procedure.pdf`

---

## 5. Operation & Maintenance

### 5.1 Normal Operation

#### Daily Checks (Automated via Monitoring System)
- Battery state of charge (SoC)
- Solar production levels
- AC output voltage and frequency
- System temperatures
- Alarm status

#### Weekly Checks (Manual)
- Visual inspection of solar panels (cleanliness, damage)
- Check for loose connections or corrosion
- Verify ventilation pathways are clear
- Review energy production logs

#### Monthly Checks
- Download and review performance data
- Clean solar panels if necessary
- Inspect battery enclosure (look for leaks, swelling)
- Test emergency shutdown procedures
- Update firmware if available

### 5.2 Preventive Maintenance Schedule

#### Every 6 Months (PG-U01 only)
**Tasks:**
- Comprehensive system inspection
- Thermal imaging of electrical connections
- Battery capacity test (discharge/recharge cycle)
- Inverter filter cleaning/replacement
- Software updates and configuration backup
- Detailed performance report

**Duration:** 4-6 hours on-site  
**Recommended:** Annual maintenance contract

#### Annual Maintenance (PG-M01, PG-P01)
**Tasks:**
- Full electrical inspection and testing
- Insulation resistance testing
- Battery management system diagnostics
- Solar panel I-V curve testing
- Inverter calibration check
- Update configuration and documentation
- Replace consumables (filters, fuses)

**Duration:** 3-4 hours on-site  
**Cost:** €2,000-€6,000 (depending on model)

#### 18-Month Maintenance (PG-C01)
**Tasks:**
- Basic inspection and cleaning
- Battery health check
- Connection torque verification
- Software updates
- Performance verification

**Duration:** 1-2 hours on-site  
**Cost:** €500-€800

#### 24-Month Maintenance (PG-M02)
**Tasks:**
- Visual inspection
- Battery voltage check
- Connection cleaning
- Firmware update

**Duration:** 30-60 minutes  
**Cost:** €200-€400

### 5.3 Cleaning and Care

#### Solar Panel Cleaning
**Frequency:** As needed (typically 2-4 times per year)  
**Method:** 
- Use soft brush or squeegee with water
- Clean in early morning or late evening (avoid hot panels)
- Do NOT use abrasive cleaners or high-pressure washers
- Professional cleaning recommended for large arrays

#### Ventilation Maintenance
- Keep air intakes/exhausts clear of debris
- Check fan operation monthly
- Replace air filters per schedule (typically 6-12 months)

### 5.4 Seasonal Considerations

#### Summer Operation
- Monitor battery temperatures closely (>40°C triggers throttling)
- Ensure adequate ventilation and shade for electronics
- Solar production at peak - excellent time for capacity testing
- Check for vegetation growth around panels

#### Winter Operation
- Reduced solar production - monitor autonomy more closely
- Remove snow from panels promptly (use soft tools)
- Battery charging may be slower in cold weather
- Keep battery temperature above 0°C (heaters may activate)

---

## 6. Troubleshooting Guide

### 6.1 Common Issues and Solutions

#### Problem: System Won't Power On
**Possible Causes:**
1. Battery discharged below cutoff voltage
2. Main disconnect switch is OFF
3. Fuse or circuit breaker tripped
4. BMS in protective shutdown mode

**Solutions:**
1. Check battery voltage (minimum 42V for 48V system)
2. Verify all disconnect switches are ON
3. Inspect and reset circuit breakers
4. Check BMS error codes via app
5. If battery critically low, connect solar or grid charging

**Reference:** `Manual_[MODEL]_vX.X.pdf` Section 8: Troubleshooting

---

#### Problem: Low Solar Charging
**Possible Causes:**
1. Panels are shaded or dirty
2. Incorrect panel orientation
3. Damaged or disconnected cables
4. MPPT controller fault

**Solutions:**
1. Inspect panels for shading, dirt, or debris - clean if necessary
2. Verify panel orientation and tilt
3. Check all solar cable connections at panels and controller
4. Measure open-circuit voltage of solar array (should match rated Voc)
5. Review MPPT controller status via monitoring app
6. If Voc is correct but charging is low, contact technical support

---

#### Problem: Battery Not Charging Fully
**Possible Causes:**
1. Insufficient solar input
2. BMS protecting cells (over-temperature, cell imbalance)
3. Incorrect charging parameters
4. Battery approaching end of life

**Solutions:**
1. Verify solar system is producing expected power
2. Check battery temperature (should be 10-35°C for optimal charging)
3. Review BMS diagnostics for cell voltage balance
4. Wait for BMS balancing cycle to complete (may take 24-48 hours)
5. If problem persists, schedule battery capacity test

---

#### Problem: Inverter Overload Error
**Possible Causes:**
1. Connected load exceeds rated capacity
2. High inrush current from motor loads
3. Inverter temperature too high
4. Inverter fault

**Solutions:**
1. Calculate total connected load - reduce if necessary
2. Stagger startup of motor loads (compressors, pumps)
3. Ensure adequate ventilation around inverter
4. Check inverter temperature display
5. If overload persists with appropriate load, contact technical support

**Advanced Setting:** Increase PowerAssist threshold (if applicable)

---

#### Problem: System Runs on Generator More Than Expected (Hybrid Mode)
**Possible Causes:**
1. Hybrid start/stop thresholds set too conservatively
2. Insufficient battery capacity for load
3. Solar charging inadequate
4. Battery degradation

**Solutions:**
1. Review and adjust hybrid mode settings:
   - Lower generator start SoC threshold (try 30% → 20%)
   - Raise generator stop SoC threshold (try 70% → 80%)
2. Audit daily energy consumption vs. solar production
3. Consider battery expansion module
4. Schedule battery capacity test if system is >3 years old

**Reference:** `Hybrid_Mode_Configuration_Guide.pdf`

---

#### Problem: Monitoring App Shows "Offline"
**Possible Causes:**
1. Loss of internet connectivity (WiFi/4G)
2. Modem or router issue
3. App authentication expired
4. System in sleep mode

**Solutions:**
1. Check WiFi/4G signal strength at system location
2. Verify router is powered and functioning
3. Restart modem (power cycle for 30 seconds)
4. Log out and log back in to mobile app
5. For systems with sleep mode, wake via physical interface
6. Check if subscription is active (Premium monitoring requires annual renewal)

---

### 6.2 Error Codes

GreenPower systems use standardized error codes displayed on local interface and in monitoring app:

| Code | Severity | Meaning | Action |
|------|----------|---------|--------|
| E01 | Warning | Low Battery (< 20% SoC) | Connect charging source or reduce load |
| E02 | Alarm | Battery Temperature High | Reduce load, improve ventilation, contact support if >50°C |
| E03 | Alarm | Battery Temperature Low | Move to warmer location or activate battery heater |
| E04 | Alarm | Cell Voltage Imbalance | Allow BMS balancing cycle, contact support if persists >48h |
| E05 | Warning | Reduced Solar Output | Check for shading, dirt, or panel damage |
| E06 | Alarm | Overload Condition | Reduce connected load immediately |
| E07 | Alarm | Inverter Overtemperature | Improve ventilation, reduce load |
| E08 | Critical | Ground Fault Detected | **SHUTDOWN SYSTEM** - Contact support immediately |
| E09 | Critical | Over Voltage | **SHUTDOWN SYSTEM** - Contact support immediately |
| E10 | Warning | Under Voltage | Check grid/generator input or increase solar charging |
| E11 | Warning | Communication Loss (BMS) | Check battery connections, restart system if persists |
| E12 | Alarm | Fan Failure | Replace fan immediately, monitor temperatures |
| E13 | Warning | Firmware Update Available | Schedule update during low-demand period |
| E14 | Alarm | Battery End of Life Warning | Schedule battery replacement within 6 months |

**Response Priorities:**
- **Critical:** Immediate shutdown and expert support required
- **Alarm:** Address within 24 hours
- **Warning:** Address at next opportunity, monitor status

---

### 6.3 When to Contact Technical Support

**Immediate Contact Required:**
- Critical error codes (E08, E09)
- Smoke, burning smell, or visible damage
- Ground fault or electrical shock hazard
- System shutdown with no clear cause
- Unusual noises from battery or inverter

**Next-Business-Day Contact:**
- Persistent alarm conditions (>48 hours)
- Performance degradation >20% from baseline
- Monitoring system completely offline >72 hours
- Battery capacity test shows <70% of rated capacity

**Contact Methods:**
- **24/7 Emergency:** +33 4 68 XX XX XX (Option 1)
- **Technical Support:** support@greenpower.com
- **Remote Diagnostics:** Via monitoring app "Request Support" button

**Information to Provide:**
- System serial number (label on unit)
- Model number
- Current error codes
- Recent operating history
- Photos/video of any visible issues

---

## 7. Safety & Compliance

### 7.1 Safety Warnings

⚠️ **ELECTRICAL HAZARD - DANGER OF DEATH** ⚠️

GreenPower systems contain:
- **High DC voltage** (up to 600V in solar arrays)
- **High stored energy** (up to 2,000 kWh in batteries)
- **AC mains voltage** (230V single-phase or 400V three-phase)

**ONLY qualified, licensed electricians may perform installation, maintenance, or repairs.**

---

#### DC Voltage Safety
- **Solar panels generate voltage in daylight - ALWAYS LIVE**
- Wear insulated gloves (rated 1000V) when working on DC circuits
- Use insulated tools
- Do not touch exposed terminals or conductors
- Cover panels or work at night when possible

#### Battery Safety
- **Do not short-circuit battery terminals** (risk of explosion/fire)
- **Do not open battery enclosures** (hydrogen gas may be present)
- Wear appropriate PPE: safety glasses, insulated gloves
- Keep sparks, flames, and smoking materials away from batteries
- In case of battery fire, use Class D fire extinguisher or dry sand (NOT water)

#### AC Safety
- De-energize AC circuits before work using lockout/tagout procedures
- Verify absence of voltage with multimeter before touching
- Follow NF C18-510 (France) or equivalent electrical safety standards
- Maintain minimum clearances per local electrical codes

---

### 7.2 Environmental & Disposal

#### Battery Disposal
GreenPower uses lithium-ion batteries which must be recycled properly:
- **DO NOT dispose in regular waste**
- **DO NOT incinerate**
- Contact GreenPower support for end-of-life battery collection
- We partner with certified EU battery recyclers
- Typical recovery rate: >95% of materials

#### E-Waste Disposal
Electronic components (inverters, controllers) are WEEE Directive compliant:
- Return to GreenPower for proper recycling
- Alternatively, use certified e-waste collection center
- Removal of system qualifies for end-of-life support service

#### Solar Panel Recycling
Crystalline silicon panels are >95% recyclable:
- Glass, aluminum frame, and silicon can be recovered
- EU PV Cycle program member
- Collection service available through GreenPower

---

### 7.3 Regulatory Compliance

#### French Regulations
- **NF C15-100:** Electrical installations (low voltage)
- **NF C14-100:** Grid connections
- **CONSUEL Attestation:** Required for grid-tied systems
- **ZFE Compliance:** Zero emissions certification for low-emission zones
- **ICPE Declaration:** If battery capacity >600 kWh (industrial sites)

#### European Directives
- **CE Marking:** All products certified
- **LVD (Low Voltage Directive):** 2014/35/EU
- **EMC (Electromagnetic Compatibility):** 2014/30/EU
- **RoHS (Restriction of Hazardous Substances):** 2011/65/EU
- **Battery Regulation:** 2023/1542 (Second-life battery provisions)

#### Radio Equipment (Monitoring Devices)
- **RED (Radio Equipment Directive):** 2014/53/EU
- FCC Part 15 (USA export models)
- Frequency bands: 868 MHz (EU), 2.4 GHz WiFi, LTE bands 3/7/20

---

### 7.4 Insurance and Liability

#### Equipment Insurance
- Recommended: All-risk equipment insurance
- Coverage should include: theft, damage, natural disasters, business interruption
- Declare equipment value and serial numbers to insurer
- GreenPower can provide valuation documents for insurance purposes

#### Liability Insurance
- Professional indemnity insurance recommended for operators
- Third-party liability coverage for event/rental applications
- Check with insurer for coverage exclusions (natural disasters, war, etc.)

#### Warranty Limitations
GreenPower warranty covers manufacturing defects only, and does NOT cover:
- Damage from improper installation, use, or maintenance
- Lightning strikes or power surges (surge protection recommended)
- Physical damage from accidents, vandalism, or natural disasters
- Unauthorized modifications or repairs
- Normal wear and tear (consumables)

---

## 8. Performance Optimization

### 8.1 Solar Panel Optimization

#### Orientation and Tilt
**Optimal Configuration for Perpignan, France (42.7°N):**
- **Azimuth:** 180° (Due South)
- **Tilt Angle:** 
  - Year-round optimal: 38-42°
  - Summer bias (May-Aug): 25-30°
  - Winter bias (Nov-Feb): 50-55°

**Shading Analysis:**
- Use solar pathfinder or mobile app to analyze site
- Avoid shading during peak sun hours (10:00-14:00)
- Even partial shading can reduce string output by 50%+
- Consider micro-inverters or power optimizers if shading is unavoidable

#### Cleaning Schedule
**Recommended Frequency:**
- Urban areas: Every 2-3 months
- Rural areas: Every 4-6 months
- Agricultural areas (high dust): Monthly during dry season
- Coastal areas (salt spray): Every 6-8 weeks

**Cleaning Method:**
- Use deionized or soft water + soft brush
- Clean in early morning or evening (avoid thermal shock)
- Do NOT use abrasive cleaners, detergents, or high-pressure washers
- Professional cleaning for large arrays (>50 panels)

**Expected Performance Impact:**
- Clean panels: 100% rated output
- Light dust (1-2 months): 95-98% output
- Moderate dirt (3-6 months): 85-92% output
- Heavy soiling: 70-85% output

---

### 8.2 Battery Management

#### Optimal Operating Conditions
- **Temperature:** 15-25°C for maximum lifespan
- **State of Charge:** Keep between 20-80% for daily cycling
  - Going to 100% occasionally (once/week) helps with balancing
  - Avoid dropping below 10% regularly
- **Depth of Discharge:** Shallower cycles = longer life
  - 50% DoD: ~5,000 cycles
  - 80% DoD: ~3,000 cycles
  - 100% DoD: ~2,000 cycles

#### Extending Battery Life
1. **Minimize high-discharge events** - Size system appropriately
2. **Keep batteries cool** - Ensure adequate ventilation
3. **Allow full charge regularly** - Once per week minimum
4. **Avoid full discharges** - Stop loads before hitting 10% SoC
5. **Maintain charging** - Don't leave battery depleted for extended periods

#### Storage Recommendations
If system will be unused for >1 month:
1. Charge battery to 50-60% SoC
2. Disconnect loads (keep monitoring active)
3. Ensure solar panels can provide maintenance charge
4. Check monthly and recharge if SoC drops below 40%

---

### 8.3 Load Management Strategies

#### Peak Shaving
For grid-tied systems, reduce grid consumption during peak hours:
1. Configure time-of-use schedule in system settings
2. Use battery during expensive peak hours (typically 18:00-21:00)
3. Recharge from grid during cheap off-peak hours (02:00-06:00)
4. Solar charging has priority during daylight

**Savings Potential:** 30-50% reduction in electricity costs

#### Load Prioritization
For off-grid systems, program essential vs. non-essential loads:
1. **Critical Loads** (priority 1): Refrigeration, security, communications
2. **Important Loads** (priority 2): Lighting, water pumps
3. **Deferrable Loads** (priority 3): Washing machines, EV charging, heating

Configure automatic load shedding thresholds:
- <30% SoC: Disable priority 3 loads
- <20% SoC: Disable priority 2 loads
- <10% SoC: Critical loads only

#### Demand Response Integration
For commercial applications:
- Participate in grid demand response programs
- Receive payment for reducing grid consumption during peak events
- System can automatically respond to utility signals
- Typical incentive: €50-200 per event (4-8 events per year)

**Reference:** `Demand_Response_Configuration_Guide.pdf`

---

### 8.4 Hybrid System Optimization

#### Generator Start/Stop Thresholds
**Conservative Settings (maximum backup):**
- Start generator: 40% battery SoC
- Stop generator: 80% battery SoC
- Result: ~85% fuel savings

**Aggressive Settings (maximum solar utilization):**
- Start generator: 20% battery SoC
- Stop generator: 60% battery SoC
- Result: ~95% fuel savings
- Risk: Less backup margin for sudden loads

**Weather-Adaptive Settings:**
- Cloudy forecast: Use conservative settings
- Sunny forecast: Use aggressive settings
- GreenPower Connect app can automate this

#### Load Sharing Configuration
Set generator power threshold for hybrid assist:
- Example: 150 kVA load on 180 kVA system
- Configure generator to start at 140 kVA load
- Prevents battery deep discharge during load spikes
- Generator runs only as long as needed (10-30 minutes typical)

---

## 9. Technical Support

### 9.1 Support Tiers

#### Standard Support (Included with Purchase)
- Email support (support@greenpower.com)
- Response time: 24-48 hours
- Phone support: Business hours (09:00-18:00 CET)
- Remote diagnostics via monitoring system
- Online knowledge base and video tutorials
- Quarterly performance reports

#### Premium Support (Subscription)
**Cost:** €500-5,000/year (depending on model)

**Includes:**
- 24/7 emergency phone support
- Priority response (<4 hours)
- Proactive monitoring and alerts
- Quarterly preventive health checks
- Predictive maintenance recommendations
- Annual on-site inspection (one visit included)
- Advanced analytics and optimization suggestions
- Dedicated technical account manager

#### Enterprise Support (Large Deployments)
**For:** >10 systems or critical infrastructure

**Includes:** Everything in Premium, plus:
- On-site technician availability (regional hubs)
- Custom SLA agreements
- Integration with client IT/BMS systems
- Training programs for client technical staff
- Disaster recovery planning
- Extended warranty options (up to 10 years)

**Contact:** enterprise@greenpower.com

---

### 9.2 Training Programs

#### Operator Training
**Duration:** 2-4 hours  
**Cost:** Included with installation  
**Topics:**
- Basic system operation
- Monitoring and interpretation
- Routine maintenance tasks
- Emergency procedures
- Troubleshooting simple issues

#### Advanced Technician Training
**Duration:** 2 days  
**Cost:** €800/person  
**Prerequisites:** Licensed electrician with 5+ years experience

**Topics:**
- In-depth system architecture
- Electrical theory and calculations
- Battery management systems
- Inverter programming and configuration
- Advanced troubleshooting
- Component replacement procedures
- Safety procedures and PPE
- Hands-on practical exercises

**Certification:** Upon completion, technicians receive GreenPower Certified Installer certificate

#### Fleet Manager Training
**Duration:** 1 day  
**Cost:** €500/person  
**For:** Rental companies, event agencies with multiple systems

**Topics:**
- Multi-system monitoring
- Fleet performance analytics
- Preventive maintenance scheduling
- Rental preparation and inspection
- Customer training best practices
- Business optimization strategies

---

### 9.3 Spare Parts and Consumables

#### Commonly Replaced Parts
| Part | Typical Lifespan | Part Number | Price (€) |
|------|------------------|-------------|-----------|
| Cooling Fan (80mm) | 3-5 years | GP-FAN-80 | 45 |
| Air Filter | 6-12 months | GP-FILTER-01 | 20 |
| Fuse 400A (DC) | As needed | GP-FUSE-400DC | 85 |
| Circuit Breaker 63A (AC) | 10+ years | GP-CB-63AC | 120 |
| Display Screen (5") | 5-10 years | GP-LCD-5 | 280 |
| Communication Modem | 5-7 years | GP-MODEM-4G | 350 |
| Temperature Sensor | 5-10 years | GP-TEMP-01 | 45 |

#### Battery Replacement
- **Second-Life EV Modules:** €200-350/kWh (installed)
- **New LiFePO4 Cells:** €300-500/kWh (installed)
- **Complete Battery Pack:**
  - PG-M02 (20 kWh): €6,000-8,000
  - PG-C01 (96 kWh): €28,000-38,000
  - PG-P01 (320 kWh): €85,000-120,000
  - PG-M01 (720 kWh): €180,000-250,000
  - PG-U01 (2,000 kWh): €450,000-600,000

**Note:** Prices include labor, testing, and disposal of old batteries

#### Ordering Parts
- **Online:** parts.greenpower.com (login required)
- **Email:** parts@greenpower.com
- **Phone:** +33 4 68 XX XX XX (Option 3)

**Shipping:**
- France mainland: 2-3 business days
- Corsica / DOM-TOM: 5-7 business days
- International: 7-14 business days
- Emergency overnight shipping available (+€150)

---

## 10. Appendices

### Appendix A: Glossary of Terms

**AC (Alternating Current):** Type of electrical current that reverses direction periodically, standard for mains power (230V/400V in Europe).

**BMS (Battery Management System):** Electronic system that monitors and protects battery cells from overcharge, overdischarge, and thermal issues.

**CAN Bus:** Controller Area Network, a communication protocol used for inter-device communication in vehicles and industrial systems.

**CE Mark:** European conformity marking indicating product meets EU safety, health, and environmental requirements.

**DoD (Depth of Discharge):** Percentage of battery capacity that has been used. 50% DoD means battery is half discharged.

**DC (Direct Current):** Type of electrical current that flows in one direction, produced by batteries and solar panels.

**Grid-Tie:** Connection to the electrical utility grid, allowing export of excess solar production or import during shortages.

**Hybrid Mode:** Operating configuration where solar/battery system is supplemented by a backup generator (typically diesel).

**Inverter:** Electronic device that converts DC electricity (from batteries/solar) to AC electricity (for appliances).

**kVA (kilovolt-ampere):** Unit of apparent electrical power, approximately equal to kW for most loads (when power factor is near 1.0).

**kW (kilowatt):** Unit of real electrical power, 1 kW = 1,000 watts.

**kWh (kilowatt-hour):** Unit of energy, amount of power used over time. Example: 1 kW load running for 1 hour consumes 1 kWh.

**kWp (kilowatt-peak):** Rated output power of solar panels under standard test conditions (1000 W/m² irradiance, 25°C cell temperature).

**MPPT (Maximum Power Point Tracking):** Advanced solar charge controller technology that optimizes power extraction from solar panels.

**NMC (Nickel Manganese Cobalt):** Type of lithium-ion battery chemistry used in many electric vehicles.

**LiFePO4 (Lithium Iron Phosphate):** Type of lithium-ion battery chemistry known for long life and safety, used in stationary storage applications.

**SoC (State of Charge):** Percentage of battery capacity currently available, similar to fuel gauge. 100% = fully charged.

**SoH (State of Health):** Indicator of battery condition relative to new, expressed as percentage. 90% SoH means battery holds 90% of original capacity.

**Three-Phase Power:** AC electrical system with three voltage waveforms offset by 120°, standard for industrial equipment (400V in Europe).

**ZFE (Zone à Faibles Émissions):** Low Emission Zone, urban area in France with restrictions on polluting vehicles and equipment.

---

### Appendix B: Cable Sizing Tables

#### DC Cable Sizing (48V Systems)

Maximum current based on continuous load:

| Load (kW) | Current (A) | Cable Size (mm²) | Max Length (m) |
|-----------|-------------|------------------|----------------|
| 1 | 21 | 6 | 25 |
| 2 | 42 | 10 | 25 |
| 3 | 63 | 16 | 25 |
| 5 | 104 | 25 | 25 |
| 10 | 208 | 50 | 15 |
| 15 | 313 | 70 | 10 |
| 20 | 417 | 95 | 10 |

**Notes:**
- Based on 3% voltage drop maximum
- For longer cable runs, increase cable size or reduce load
- Use copper conductors only (never aluminum for DC)
- For solar panel strings, use UV-resistant, double-insulated cable

#### AC Cable Sizing (Single Phase 230V)

| Load (kW) | Current (A) | Cable Size (mm²) | MCB Rating (A) |
|-----------|-------------|------------------|----------------|
| 1 | 4.3 | 1.5 | 10 |
| 2 | 8.7 | 2.5 | 16 |
| 3 | 13 | 2.5 | 16 |
| 5 | 22 | 6 | 32 |
| 10 | 43 | 10 | 50 |
| 15 | 65 | 16 | 80 |
| 20 | 87 | 25 | 100 |

#### AC Cable Sizing (Three Phase 400V)

| Load (kW) | Current (A) | Cable Size (mm²) | MCB Rating (A) |
|-----------|-------------|------------------|----------------|
| 5 | 7.2 | 2.5 | 16 |
| 10 | 14.4 | 2.5 | 20 |
| 20 | 29 | 6 | 32 |
| 30 | 43 | 10 | 50 |
| 50 | 72 | 16 | 80 |
| 75 | 108 | 25 | 125 |
| 100 | 144 | 50 | 160 |

**Notes:**
- Based on NF C15-100 installation method B (conduit in insulated wall)
- For other installation methods, refer to electrical code tables
- MCB (Miniature Circuit Breaker) ratings are standard values
- Always include RCD (Residual Current Device) protection: 30mA for circuits ≤32A

---

### Appendix C: Performance Calculation Examples

#### Example 1: Sizing a System for a Construction Site

**Requirements:**
- Concrete mixer: 15 kW (intermittent, 4 hours/day)
- Power tools: 5 kW (intermittent, 6 hours/day)
- Site office: 2 kW (continuous, 10 hours/day)
- Lighting: 1 kW (6 hours/day)
- Location: Perpignan, France

**Daily Energy Consumption:**
- Mixer: 15 kW × 4 h = 60 kWh
- Tools: 5 kW × 6 h = 30 kWh
- Office: 2 kW × 10 h = 20 kWh
- Lighting: 1 kW × 6 h = 6 kWh
- **Total: 116 kWh/day**

**Peak Power:**
- Mixer + Tools + Office + Lighting = 23 kW (not all simultaneous)
- Realistic peak: 20 kW (mixer + office + partial tools)
- **Required capacity: 25 kVA minimum** (25% safety margin)

**Recommended System:** **PG-P01 (Performance)**
- Capacity: 80 kVA continuous ✓
- Battery: 320 kWh (2.8 days autonomy at average load) ✓
- Solar: 24 kWp (generates ~100-120 kWh/day in summer, 40-60 kWh/day in winter)

**Winter Considerations:**
- Reduced solar production may not meet 116 kWh/day demand
- Options:
  1. Add PG-ACC-01 Extended Solar Array (+25% production)
  2. Enable hybrid mode with small diesel generator (PG-ACC-03)
  3. Reduce non-essential loads in winter months

**Investment:**
- PG-P01 system: €75,000
- Diesel fuel savings: ~€12,000/year (100L/day @ €1.60/L × 250 days)
- **Payback period: ~6 years**

---

#### Example 2: Powering a Music Festival

**Requirements:**
- Main stage sound/lights: 80 kW (12 hours/day, 3 days)
- Secondary stage: 30 kW (8 hours/day, 3 days)
- Food vendors (10 units): 5 kW each (14 hours/day, 3 days)
- Backstage/facilities: 20 kW (24 hours/day, 3 days)

**Daily Energy Consumption:**
- Main stage: 80 kW × 12 h = 960 kWh
- Secondary stage: 30 kW × 8 h = 240 kWh
- Vendors: 50 kW × 14 h = 700 kWh
- Facilities: 20 kW × 24 h = 480 kWh
- **Total: 2,380 kWh/day**

**Peak Power (evening):**
- All loads active: 80 + 30 + 50 + 20 = 180 kW
- **Required capacity: 225 kVA minimum**

**Recommended System:** **2× PG-U01 + 4× PG-M01**
- Total capacity: 2×500 kVA + 4×180 kVA = 1,720 kVA ✓
- Total battery: 2×2,000 kWh + 4×720 kWh = 6,880 kWh ✓
- Total solar: 2×150 kWp + 4×48 kWp = 492 kWp

**Operational Plan:**
- PG-U01 units: Main stage + secondary stage
- PG-M01 units: Vendor area (2 units), facilities (1 unit), spare (1 unit)
- Solar charging during day supports evening loads
- Battery autonomy: ~2.9 days at full load without sun

**Cost Comparison:**
- GreenPower rental (3 days + setup/teardown): €35,000
- Diesel generator rental (180 kVA × 6 units): €18,000
- Diesel fuel (3,000L @ €1.60/L): €4,800
- **Diesel total: €22,800**
- **GreenPower premium: €12,200 (53% more)**

**Value Proposition:**
- Zero emissions (festival sustainability goals)
- Noise-free operation (better for acoustic performances)
- No fuel logistics or refueling
- Positive marketing and attendee experience
- Carbon credits (8 tonnes CO2 avoided)

---

### Appendix D: Contact Information

**GreenPower Solutions**  
123 Avenue de l'Énergie Solaire  
66000 Perpignan, France

**Main Office:**  
Tel: +33 4 68 XX XX XX  
Email: contact@greenpower.com  
Web: www.greenpower.com

**Technical Support:**  
Tel: +33 4 68 XX XX XX (Option 2)  
Email: support@greenpower.com  
Hours: 24/7 for Premium customers, M-F 9:00-18:00 for Standard

**Sales Inquiries:**  
Tel: +33 4 68 XX XX XX (Option 1)  
Email: sales@greenpower.com  
Hours: Monday-Friday 9:00-18:00 CET

**Emergency Support (24/7):**  
Tel: +33 4 68 XX XX XX (Option 9)  
For: Critical system failures, safety issues

**Parts Department:**  
Email: parts@greenpower.com  
Web: parts.greenpower.com

**Training & Education:**  
Email: training@greenpower.com  
Web: greenpower.com/training

**Social Media:**  
LinkedIn: /company/greenpower-solutions  
YouTube: @GreenPowerEnergy  
Twitter: @GreenPowerFR

---

### Appendix E: Warranty Registration

All GreenPower systems must be registered within 30 days of installation to activate full warranty coverage.

**Online Registration:** greenpower.com/warranty-registration

**Required Information:**
- System serial number (label on unit)
- Model number
- Purchase date and invoice number
- Installation date
- End-user name and contact information
- Installer name and license number (if applicable)
- Photos of installed system (4 minimum)

**What to Photograph:**
1. System nameplate (serial number visible)
2. Overall system installation
3. Solar panel array
4. Electrical connections (breaker panel)

**Registration Confirmation:**
- You will receive email confirmation within 2 business days
- Includes warranty certificate PDF
- Maintenance schedule reminders
- Access to online owner portal

---

## Document History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | March 2020 | Initial release | V. Theroux |
| 2.0 | January 2022 | Added PG-C01, PG-M02 models | Technical Team |
| 2.5 | June 2023 | Updated hybrid mode section | R. Dubois |
| 3.0 | December 2024 | Complete restructuring, added troubleshooting | Technical Team |
| 3.1 | January 2025 | Updated specifications, added examples | M. Laurent |

---

**© 2025 GreenPower Solutions. All rights reserved.**

*This document contains proprietary information and may not be reproduced without written permission from GreenPower Solutions.*

**Disclaimer:** Technical specifications subject to change without notice. Always refer to product datasheets and manuals for most current information. GreenPower Solutions is not responsible for errors or omissions in this document.
