(
echo import torch
echo import psutil
echo def get_gpu_stats(^):
echo     if torch.cuda.is_available(^):
echo         return {
echo             "vram_total": torch.cuda.get_device_properties(0^).total_memory / 1024**3,
echo             "vram_allocated": torch.cuda.memory_allocated(0^) / 1024**3,
echo             "utilization": "monitoring via nvml..."
echo         }
echo     return {"error": "CUDA not available"}
) > src/hardware_monitor.py
