class_name VisualSettings extends Resource

var screen_modes: Array = [
	"fullscreen", 
	"windowed", 
	"maximized"
	]
	
var resolutions: Array[Vector2i] = [
	Vector2i(1920, 1080), 
	Vector2i(2560, 1440), 
	Vector2i(1280, 720)
	]

@export var screen_mode_index: int = 0
@export var resolution_index: int = 0
@export var vsync: bool = false

var anti_aliasing: String
var cap_fps: bool
var quality
