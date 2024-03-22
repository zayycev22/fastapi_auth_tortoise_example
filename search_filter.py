from typing import List, Tuple

from fastapi_auth.filters import SearchFilter


class TortoiseSearchFilter(SearchFilter):
    async def _get_instance(self, field_names: List[str], instance: object) -> Tuple[str, object]:
        for i in range(len(field_names) - 1):
            instance = await getattr(instance, field_names[i])
            if instance is None:
                return field_names[-1], None
        return field_names[-1], instance
