extends Control

@export var gameplay_tab_button: Button
@export var gameplay_tab: PanelContainer
@export var video_tab: PanelContainer
@export var audio_tab: PanelContainer
@export var keybinds_tab: PanelContainer

signal close_settings()


func _ready():
	gameplay_tab.visible = true
	video_tab.visible = false
	audio_tab.visible = false
	keybinds_tab.visible = false
	gameplay_tab_button.set_pressed(true)
	
func switch_tab(tab: String) -> void:
	gameplay_tab.visible = false
	video_tab.visible = false
	audio_tab.visible = false
	keybinds_tab.visible = false
	
	if tab == "gameplay_tab":
		gameplay_tab.visible = true
	elif tab == "video_tab":
		video_tab.visible = true
	elif tab == "audio_tab":
		audio_tab.visible = true
	elif tab == "keybinds_tab":
		keybinds_tab.visible = true

func _on_exit_pressed():
	visible = false
	emit_signal("close_settings")

func _on_video_tab_button_pressed():
	switch_tab("video_tab")

func _on_gameplay_tab_button_pressed():
	switch_tab("gameplay_tab")

func _on_audio_tab_button_pressed():
	switch_tab("audio_tab")

func _on_keybinds_tab_button_pressed():
	switch_tab("keybinds_tab")
