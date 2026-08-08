from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

# Parking data
slots = {}
for i in range(1, 11):
    slots[i] = {
        "slot_id": i,
        "status": "free",
        "vehicle_number": None,
        "entry_time": None
    }

HOURLY_RATE = 2
MINIMUM_FEE = 1

@app.route('/')
def home():
    return jsonify({
        "message": "Smart Parking System API is running!",
        "endpoints": {
            "/slots": "GET - View all slots",
            "/slots/free": "GET - View free slots only",
            "/entry": "POST - Vehicle entry (send vehicle_number)",
            "/exit": "POST - Vehicle exit (send vehicle_number)",
            "/status": "GET - System summary"
        }
    })

@app.route('/slots')
def get_slots():
    slots_list = []
    for slot_num, info in slots.items():
        slots_list.append({
            "slot_id": slot_num,
            "status": info["status"],
            "vehicle_number": info["vehicle_number"]
        })
    return jsonify({
        "success": True,
        "total_slots": len(slots_list),
        "slots": slots_list
    })

@app.route('/slots/free')
def get_free_slots():
    free_slots = []
    for slot_num, info in slots.items():
        if info["status"] == "free":
            free_slots.append(slot_num)
    return jsonify({
        "success": True,
        "free_slots_count": len(free_slots),
        "free_slots": free_slots
    })

@app.route('/entry', methods=['POST'])
def vehicle_entry():
    data = request.get_json()
    
    if not data or 'vehicle_number' not in data:
        return jsonify({"success": False, "message": "Vehicle number required"}), 400
    
    vehicle_number = data['vehicle_number']
    
    for slot_num in range(1, 11):
        if slots[slot_num]["status"] == "free":
            slots[slot_num]["status"] = "taken"
            slots[slot_num]["vehicle_number"] = vehicle_number
            slots[slot_num]["entry_time"] = datetime.datetime.now().isoformat()
            
            return jsonify({
                "success": True,
                "vehicle_number": vehicle_number,
                "assigned_slot": slot_num,
                "message": f"Go to Slot {slot_num}"
            })
    
    return jsonify({"success": False, "message": "Parking full!"}), 404

@app.route('/exit', methods=['POST'])
def vehicle_exit():
    data = request.get_json()
    
    if not data or 'vehicle_number' not in data:
        return jsonify({"success": False, "message": "Vehicle number required"}), 400
    
    vehicle_number = data['vehicle_number']
    
    for slot_num, info in slots.items():
        if info["vehicle_number"] == vehicle_number:
            entry_time = datetime.datetime.fromisoformat(info["entry_time"])
            exit_time = datetime.datetime.now()
            
            duration_minutes = (exit_time - entry_time).total_seconds() / 60
            duration_hours = duration_minutes / 60
            
            fee = duration_hours * HOURLY_RATE
            if fee < MINIMUM_FEE:
                fee = MINIMUM_FEE
            
            info["status"] = "free"
            info["vehicle_number"] = None
            info["entry_time"] = None
            
            return jsonify({
                "success": True,
                "vehicle_number": vehicle_number,
                "duration_minutes": round(duration_minutes, 2),
                "total_amount": round(fee, 2),
                "message": f"Total amount: ${round(fee, 2)}"
            })
    
    return jsonify({"success": False, "message": "Vehicle not found"}), 404

@app.route('/status')
def system_status():
    free_count = 0
    occupied_count = 0
    
    for info in slots.values():
        if info["status"] == "free":
            free_count += 1
        else:
            occupied_count += 1
    
    return jsonify({
        "success": True,
        "total_slots": 10,
        "occupied_slots": occupied_count,
        "free_slots": free_count
    })

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚗 SMART PARKING SYSTEM API")
    print("="*50)
    print("\n✅ API is running on your desktop!")
    print("🌐 Open in browser: http://127.0.0.1:5000")
    print("\n📋 Test these URLs:")
    print("   http://127.0.0.1:5000/slots")
    print("   http://127.0.0.1:5000/slots/free")
    print("   http://127.0.0.1:5000/status")
    print("\n⏹️  Press CTRL+C to stop")
    print("="*50 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)
