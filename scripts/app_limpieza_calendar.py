import os
import sys

file_path = r'g:\Otros ordenadores\Mi MacBook Pro\Desktop\joan\mint-fresh-app\src\features\dashboard\presentation\pages\ScheduleManagementScreen.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_code = """                {showPicker && (
                    <DateTimePicker
                        testID="dateTimePicker"
                        value={date}
                        mode={mode}
                        is24Hour={true}
                        display={Platform.OS === 'ios' ? 'inline' : 'default'}
                        onChange={onChangeDate}
                    />
                )}"""

new_code = """                {showPicker && (
                    Platform.OS === 'web' ? (
                        <input
                            type="datetime-local"
                            value={new Date(date.getTime() - date.getTimezoneOffset() * 60000).toISOString().slice(0, 16)}
                            onChange={(e) => {
                                const val = e.target.value;
                                if (val) {
                                    setDate(new Date(val));
                                    setDateSelected(true);
                                    setShowPicker(false);
                                }
                            }}
                            style={{
                                padding: 12,
                                borderRadius: 8,
                                border: '1px solid #E0E0E0',
                                fontSize: 16,
                                marginTop: 16,
                                width: '100%',
                                outline: 'none',
                                boxSizing: 'border-box'
                            }}
                        />
                    ) : (
                        <DateTimePicker
                            testID="dateTimePicker"
                            value={date}
                            mode={mode}
                            is24Hour={true}
                            display={Platform.OS === 'ios' ? 'inline' : 'default'}
                            onChange={onChangeDate}
                        />
                    )
                )}"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Updated the DateTimePicker for web compatibility.")
else:
    print("ERROR: Could not find the expected code block in ScheduleManagementScreen.js.")
    sys.exit(1)
