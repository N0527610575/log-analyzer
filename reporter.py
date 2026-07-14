
import checks
def reporter(log_data,print_file,dict_analyz):
    with open(print_file,"w",encoding="utf-8")as file:

        file.write("=" * 30 + "\n")
        file.write("דוח תעבורה חשודה" + "\n")
        file.write("=" * 30 + "\n")

        file.write("")
        file.write("")
        file.write(   "  סטטיטיסטיקות כלליות"  + "\n")
        file.write(f"שורות שנקראו  {len(log_data)}" + "\n")
        file.write(f"שורות חשודות  {len(checks.safe_port(log_data))}" + "\n")
        file.write(f"")
        file.write(f"")


        for tag, count in checks.lists_tag(dict_analyz).items():
            file.write("=" * 30+ "\n")
            file.write(f"{tag}: {count}\n")
        file.write("=" * 30+ "\n")


        for ip, tags in checks.analyze_logs_to_dict(log_data).items():

            if len(tags) >= 3:
                file.write(f"חשודים גדולים" + "\n")
                file.write(f"{ip}" + "\n")
        file.write("=" * 30 + "\n")

        for ip, tags in checks.analyze_logs_to_dict(log_data).items():
            if len(tags) < 3:
                file.write( "חשודים נוספים" + "\n")
                file.write(f"{ip}")
        file.write("=" * 30 + "\n")








