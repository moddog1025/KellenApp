extends PanelContainer

@onready var keybind_button = preload("res://Scenes/UI/Menus/keybinds_mapping_button.tscn")
@onready var action_list = $"MarginContainer/VBoxContainer/ScrollContainer/Action List"

var is_remapping = false
var action_to_remap = null
var remapping_button = null

var input_actions = {
	"move_forward": "Forward",
	"move_backward": "Backward",
	"move_left": "Left",
	"move_right": "Right",
	"sprint": "Sprint",
	"jump": "Jump",
	"crouch": "Crouch",
	"slide": "Slide",
	"shoot": "Shoot",
	"aim": "Aim",
	"reload": "Reload",
	"interact": "Interact",
	"scoreboard": "Scoreboard",
}


func _ready():
	load_keybinds_from_settings()
	create_action_list()
	
func load_keybinds_from_settings():
	var keybinds = ConfigHandler.load_keybinds()
	for action in keybinds.keys():
		InputMap.action_erase_events(action)
		InputMap.action_add_event(action, keybinds[action])


func create_action_list():
	for item in action_list.get_children():
		item.queue_free()
	
	for action in input_actions:
		var button = keybind_button.instantiate()
		var action_label = button.find_child("Action Label")
		var input_label = button.find_child("Key Label")
		
		action_label.text = input_actions[action]
		
		var events = InputMap.action_get_events(action)
		if events.size() > 0:
			input_label.text = events[0].as_text().trim_suffix(" (Physical)")
			if input_label.text.contains("L"):
				input_label = "LMB"
			elif input_label.text.contains("R"):
				input_label = "RMB"
		else:
			input_label.text = ""
			
		action_list.add_child(button)
		button.pressed.connect(_on_input_button_pressed.bind(button, action))
		
func _on_input_button_pressed(button, action):
	if !is_remapping:
		is_remapping = true
		action_to_remap = action
		remapping_button = button
		button.find_child("Key Label").text = "Press key..."
		
func _input(event):
	if is_remapping:
		if (event is InputEventKey or (event is InputEventMouseButton and event.pressed)):
				
				if event is InputEventMouseButton and event.double_click:
					event.double_click = false
					
				InputMap.action_erase_events(action_to_remap)
				ConfigHandler.save_keybind(action_to_remap, event)
				InputMap.action_add_event(action_to_remap, event)
				update_action_list(remapping_button, event)
				
				is_remapping = false
				action_to_remap = null
				remapping_button = null
				
				accept_event()
				
func update_action_list(button, event):
	button.find_child("Key Label").text = event.as_text().trim_suffix(" (Physical)")

func _on_reset_button_pressed():
	InputMap.load_from_project_settings()
	for action in input_actions:
		var events = InputMap.action_get_events(action)
		if events.size() > 0:
			ConfigHandler.save_keybind(action, events[0])
	create_action_list()
