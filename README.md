# 📦 tomoplex-bendingmachine

Ein Python- und Arduino-basiertes System zur Steuerung und Datenerfassung dieser Biegevorrichtung. Dieses Projekt ermöglicht die präzise Steuerung von Motoren, das Auslesen von Kraft- und Impedanzmessungen sowie die automatisierte Datenspeicherung für Materialtests und -analysen. 
Klone das Repository auf den Pi und installiere alle Abhängigkeiten.

---

### 🔧 Funktionen

* **Motorsteuerung**: Präzise Ansteuerung von Motoren über Arduino (`arduino_motor_controller.ino`).
* **Kraftmessung**: Integration von Wägezellen mit HX711-Modul (`hx711.py`, `load_cell.py`).
* **Impedanzmessung**: Kommunikation mit einem LCR-Meter zur Erfassung elektrischer Eigenschaften (`lcr_meter.py`).
* **Serielle Kommunikation**: Robuste Schnittstelle zwischen Python und Arduino (`arduino_com.py`, `usb_rs.py`).
* **Datenerfassung**: Automatisierte Speicherung von Messdaten in `measurement_data.txt`.
* **Hauptsteuerung**: Zentrale Ablaufsteuerung und Datenverarbeitung (`main.py`).

---

### 🛠️📡 Installation und Verwendung mit Raspberry Pi als Access Point 

Das System ist für die Ausführung auf einem **Raspberry Pi eingerichtet**, der als **Standalone Access Point** konfiguriert wurde. Um den Code dort auszuführen, gehe wie folgt vor:

1. **Mit dem Raspberry Pi WLAN verbinden**:

   * SSID: `TOMOPLEX_AP_RPI`
   * Passwort: `tomoplex`

2. **Anmelden**:

   * Melde dich an einem der eingerichteten Benutzerkonten auf dem Pi an via SSH.

3. **Einmalige Verbindung mit LAN**:

   * Verbinde den Raspberry Pi per LAN-Kabel mit dem Internet.
   * Klone das Repository auf den Pi und installiere alle Abhängigkeiten:

     ```bash
     git clone https://github.com/sKYwALK3R7/tomoplex-bendingmachine.git
     cd tomoplex-bendingmachine
     pip install pyserial
     ```

4. **LAN entfernen**:

   * Nach der Installation kann das LAN-Kabel entfernt werden.
   * Die weitere Nutzung erfolgt über das WLAN-Netzwerk des Raspberry Pi.

5. **Arduino-Code flashen**:

   > ⚠️ Der Arduino-Sketch muss **über einen Laptop mit der Arduino IDE** auf den Arduino geflasht werden (bisher noch nicht über den Raspberry Pi möglich).

   * Öffne `arduino_motor_controller.ino` mit der Arduino-IDE.
   * Wähle das passende Board und den richtigen Port.
   * Klicke auf **Hochladen**, um den Sketch zu übertragen.

---
### 🚀 Nutzung

1. **Hardware anschließen**
2. **Python-Skript starten**:

   ```bash
   python main.py
   ```

Die Steuerung läuft automatisiert, Messdaten werden in `measurement_data.txt` gespeichert.

---

### 📁 Projektstruktur

```
tomoplex-bendingmachine/
├── arduino_com.py
├── arduino_motor_controller.ino
├── hx711.py
├── lcr_meter.py
├── load_cell.py
├── main.py
├── measurement_data.txt
├── usb_rs.py
└── README.md
```

---

### 🤝 Mitwirkende

* [sKYwALK3R7](https://github.com/sKYwALK3R7)

---
