extends Node

var config = ConfigFile.new()
const settings_file_path = "user://settings.ini"

func _ready():
	if !FileAccess.file_exists(settings_file_path):
		
		#Gameplay
			#Movement
		config.set_value("gameplay", "toggle_crouch", false)
		config.set_value("gameplay", "sprint_by_default", true)
			#Debug
		config.set_value("gameplay", "show_fps", false)
		config.set_value("gameplay", "show_ping", false)
		
		#Video
		config.set_value("video", "screen_mode", 0)
		config.set_value("video", "resolution", 0)
		config.set_value("video", "vsync", false)
		config.set_value("video", "anti_aliasing_mode", 0)
		
		#Audio
		config.set_value("audio", "master_volume", 0.5)
	
		#Keybinds
			#Movement
		config.set_value("keybinds", "move_forward", "W")
		config.set_value("keybinds", "move_backward", "S")
		config.set_value("keybinds", "move_right", "D")
		config.set_value("keybinds", "move_left", "A")
		config.set_value("keybinds", "sprint", "SHIFT")
		config.set_value("keybinds", "jump", "SPACE")
		config.set_value("keybinds", "crouch", "C")
		config.set_value("keybinds", "slide", "C")
			#Utility
		config.set_value("keybinds", "shoot", "MOUSE_1")
		config.set_value("keybinds", "aim", "MOUSE_2")
		config.set_value("keybinds", "reload", "R")
		config.set_value("keybinds", "interact", "F")
			#Menus
		config.set_value("keybinds", "scoreboard", "TAB")
		config.set_value("keybinds", "menu", "ESC")
		
		config.save(settings_file_path)
		
	else:
		config.load(settings_file_path)
		
func save_gameplay_setting(key: String, value) -> void:
	config.set_value("gameplay", key, value)
	config.save(settings_file_path)
	
func load_gameplay_settings():
	var gameplay_settings = {}
	for key in config.get_section_keys("gameplay"):
		gameplay_settings[key] = config.get_value("gameplay", key)
	return gameplay_settings
	
func save_video_setting(key: String, value) -> void:
	config.set_value("video", key, value)
	config.save(settings_file_path)
	
func load_video_settings():
	var video_settings = {}
	for key in config.get_section_keys("video"):
		video_settings[key] = config.get_value("video", key)
	return video_settings
	
func save_audio_setting(key: String, value) -> void:
	config.set_value("audio", key, value)
	config.save(settings_file_path)
	
func load_audio_settings():
	var audio_settings = {}
	for key in config.get_section_keys("audio"):
		audio_settings[key] = config.get_value("audio", key)
	return audio_settings
	
func save_keybind(action: StringName, event: InputEvent) -> void:
	var event_str
	if event is InputEventKey:
		event_str = OS.get_keycode_string(event.physical_keycode)
	elif event is InputEventMouseButton:
		event_str = "MOUSE_" + str(event.button_index)
	config.set_value("keybinds", action, event_str)
	config.save(settings_file_path)
	
func load_keybinds():
	var keybinds = {}
	var keys = config.get_section_keys("keybinds")
	for key in keys:
		var input_event
		var event_str = config.get_value("keybinds", key)
		
		if event_str.contains("MOUSE_"):
			input_event = InputEventMouseButton.new()
			input_event.button_index = int(event_str.split("_")[1])
		else:
			input_event = InputEventKey.new()
			input_event.keycode = OS.find_keycode_from_string(event_str)
		
		keybinds[key] = input_event
	return keybinds
		
